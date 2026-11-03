#!/usr/bin/env python3
# Modified for this skill collection: resolve fork PRs and paginate all feedback.
"""
Fetch all PR conversation comments + reviews + review threads (inline threads)
for the PR associated with the current git branch, by shelling out to:

  gh api graphql

Requires:
  - `gh auth login` already set up
  - current branch has an associated (open) PR

Usage:
  python fetch_comments.py > pr_comments.json
"""

from __future__ import annotations

import json
import subprocess
import sys
from typing import Any
from urllib.parse import urlsplit

QUERY = """\
query(
  $owner: String!,
  $repo: String!,
  $number: Int!,
  $commentsCursor: String,
  $reviewsCursor: String,
  $threadsCursor: String,
  $fetchComments: Boolean!,
  $fetchReviews: Boolean!,
  $fetchThreads: Boolean!
) {
  repository(owner: $owner, name: $repo) {
    pullRequest(number: $number) {
      number
      url
      title
      state

      # Top-level "Conversation" comments (issue comments on the PR)
      comments(first: 100, after: $commentsCursor) @include(if: $fetchComments) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          body
          createdAt
          updatedAt
          author { login }
        }
      }

      # Review submissions (Approve / Request changes / Comment), with body if present
      reviews(first: 100, after: $reviewsCursor) @include(if: $fetchReviews) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          state
          body
          submittedAt
          author { login }
        }
      }

      # Inline review threads (grouped), includes resolved state
      reviewThreads(first: 100, after: $threadsCursor) @include(if: $fetchThreads) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          isResolved
          isOutdated
          path
          line
          diffSide
          startLine
          startDiffSide
          originalLine
          originalStartLine
          resolvedBy { login }
          comments(first: 100) {
            pageInfo { hasNextPage endCursor }
            nodes {
              id
              body
              createdAt
              updatedAt
              author { login }
            }
          }
        }
      }
    }
  }
}
"""

THREAD_COMMENTS_QUERY = """\
query($id: ID!, $cursor: String!) {
  node(id: $id) {
    ... on PullRequestReviewThread {
      comments(first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          body
          createdAt
          updatedAt
          author { login }
        }
      }
    }
  }
}
"""


def _run(cmd: list[str], stdin: str | None = None) -> str:
    p = subprocess.run(cmd, input=stdin, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{p.stderr}")
    return p.stdout


def _run_json(cmd: list[str], stdin: str | None = None) -> dict[str, Any]:
    out = _run(cmd, stdin=stdin)
    try:
        return json.loads(out)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse JSON from command output: {e}\nRaw:\n{out}") from e


def _ensure_gh_authenticated() -> None:
    try:
        _run(["gh", "auth", "status"])
    except RuntimeError:
        print("run `gh auth login` to authenticate the GitHub CLI", file=sys.stderr)
        raise RuntimeError("gh auth status failed; run `gh auth login` to authenticate the GitHub CLI") from None


def get_current_pr_ref() -> tuple[str, str, int]:
    """
    Resolve the PR for the current branch (whatever gh considers associated).
    The PR URL identifies its base repository, including for fork PRs.
    """
    pr = _run_json(["gh", "pr", "view", "--json", "number,url"])
    owner, repo = urlsplit(pr["url"]).path.strip("/").split("/")[:2]
    number = int(pr["number"])
    return owner, repo, number


def gh_api_graphql(
    query: str, **variables: str | int | bool | None
) -> dict[str, Any]:
    """
    Call `gh api graphql` using -F variables, avoiding JSON blobs with nulls.
    Query is passed via stdin using query=@- to avoid shell newline/quoting issues.
    """
    cmd = ["gh", "api", "graphql", "-F", "query=@-"]
    for name, value in variables.items():
        if value is not None:
            value = str(value).lower() if isinstance(value, bool) else value
            cmd += ["-F", f"{name}={value}"]

    payload = _run_json(cmd, stdin=query)
    if payload.get("errors"):
        raise RuntimeError(f"GitHub GraphQL errors:\n{json.dumps(payload['errors'], indent=2)}")
    return payload


def fetch_all(owner: str, repo: str, number: int) -> dict[str, Any]:
    connections: dict[str, list[dict[str, Any]]] = {
        "comments": [],
        "reviews": [],
        "reviewThreads": [],
    }
    cursors: dict[str, str | None] = dict.fromkeys(connections)
    pending = set(connections)

    pr_meta: dict[str, Any] | None = None

    while pending:
        payload = gh_api_graphql(
            QUERY,
            owner=owner,
            repo=repo,
            number=number,
            commentsCursor=cursors["comments"],
            reviewsCursor=cursors["reviews"],
            threadsCursor=cursors["reviewThreads"],
            fetchComments="comments" in pending,
            fetchReviews="reviews" in pending,
            fetchThreads="reviewThreads" in pending,
        )

        pr = payload["data"]["repository"]["pullRequest"]
        if pr_meta is None:
            pr_meta = {
                "number": pr["number"],
                "url": pr["url"],
                "title": pr["title"],
                "state": pr["state"],
                "owner": owner,
                "repo": repo,
            }

        for name in tuple(pending):
            connection = pr[name]
            connections[name].extend(connection.get("nodes") or [])
            cursors[name] = connection["pageInfo"]["endCursor"]
            if not connection["pageInfo"]["hasNextPage"]:
                pending.remove(name)

    for thread in connections["reviewThreads"]:
        comments = thread["comments"]
        page_info = comments.pop("pageInfo")
        while page_info["hasNextPage"]:
            payload = gh_api_graphql(
                THREAD_COMMENTS_QUERY, id=thread["id"], cursor=page_info["endCursor"]
            )
            page = payload["data"]["node"]["comments"]
            comments["nodes"].extend(page.get("nodes") or [])
            page_info = page["pageInfo"]

    assert pr_meta is not None
    return {
        "pull_request": pr_meta,
        "conversation_comments": connections["comments"],
        "reviews": connections["reviews"],
        "review_threads": connections["reviewThreads"],
    }


def main() -> None:
    _ensure_gh_authenticated()
    owner, repo, number = get_current_pr_ref()
    result = fetch_all(owner, repo, number)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
