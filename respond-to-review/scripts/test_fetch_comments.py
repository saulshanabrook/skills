"""Regression checks for repository selection and complete PR feedback collection."""

import unittest
from unittest.mock import patch

import fetch_comments


class FetchCommentsTests(unittest.TestCase):
    def test_fork_pr_uses_base_repository(self):
        pr = {
            "number": 42,
            "url": "https://github.com/upstream/project/pull/42",
            "headRepositoryOwner": {"login": "contributor"},
            "headRepository": {"name": "project-fork"},
        }
        with patch.object(fetch_comments, "_run_json", return_value=pr):
            self.assertEqual(fetch_comments.get_current_pr_ref(), ("upstream", "project", 42))

    def test_unequal_connection_lengths_do_not_restart_finished_pages(self):
        requests = {"comments": [], "reviews": [], "reviewThreads": []}
        calls = 0

        def fake_gh(command, stdin=None):
            nonlocal calls
            calls += 1
            self.assertLessEqual(calls, 6, "pagination failed to finish")
            variables = dict(field.split("=", 1) for field in command[4::2])
            pr = {"number": 42, "url": "https://github.com/upstream/project/pull/42",
                  "title": "Example", "state": "OPEN"}
            for name, cursor_name, include_name, page_count in (
                ("comments", "commentsCursor", "fetchComments", 2),
                ("reviews", "reviewsCursor", "fetchReviews", 3),
                ("reviewThreads", "threadsCursor", "fetchThreads", 1),
            ):
                if variables.get(include_name, "true") == "false":
                    continue
                index = int(variables.get(cursor_name, "0"))
                requests[name].append(index)
                node = {"id": f"{name}-{index}"}
                if name == "reviewThreads":
                    node["comments"] = {
                        "nodes": [{"id": "inline-comment"}],
                        "pageInfo": {"hasNextPage": False, "endCursor": "1"},
                    }
                pr[name] = {
                    "nodes": [node],
                    "pageInfo": {"hasNextPage": index + 1 < page_count,
                                 "endCursor": str(index + 1)},
                }
            return {"data": {"repository": {"pullRequest": pr}}}

        with patch.object(fetch_comments, "_run_json", side_effect=fake_gh):
            result = fetch_comments.fetch_all("upstream", "project", 42)

        self.assertEqual([node["id"] for node in result["conversation_comments"]],
                         ["comments-0", "comments-1"])
        self.assertEqual([node["id"] for node in result["reviews"]],
                         ["reviews-0", "reviews-1", "reviews-2"])
        self.assertEqual([node["id"] for node in result["review_threads"]], ["reviewThreads-0"])
        self.assertEqual(requests, {"comments": [0, 1], "reviews": [0, 1, 2], "reviewThreads": [0]})
        self.assertEqual(calls, 3)

    def test_thread_comments_include_every_page_and_preserve_output_shape(self):
        comments = [{"id": f"comment-{index}"} for index in range(205)]
        nested_cursors = []

        def fake_gh(command, stdin=None):
            variables = dict(field.split("=", 1) for field in command[4::2])
            start = int(variables.get("cursor", "0"))
            end = min(start + 100, len(comments))
            page = {"nodes": comments[start:end],
                    "pageInfo": {"hasNextPage": end < len(comments), "endCursor": str(end)}}
            if "id" in variables:
                self.assertEqual(variables["id"], "long-thread")
                nested_cursors.append(start)
                return {"data": {"node": {"comments": page}}}

            return {"data": {"repository": {"pullRequest": {
                "number": 42, "url": "https://github.com/upstream/project/pull/42",
                "title": "Example", "state": "OPEN",
                "comments": {"nodes": [], "pageInfo": {"hasNextPage": False, "endCursor": None}},
                "reviews": {"nodes": [], "pageInfo": {"hasNextPage": False, "endCursor": None}},
                "reviewThreads": {
                    "nodes": [
                        {"id": "long-thread", "isResolved": False, "comments": page},
                        {"id": "short-thread", "isResolved": True, "comments": {
                            "nodes": [{"id": "only-comment"}],
                            "pageInfo": {"hasNextPage": False, "endCursor": "1"},
                        }},
                    ],
                    "pageInfo": {"hasNextPage": False, "endCursor": "2"},
                },
            }}}}

        with patch.object(fetch_comments, "_run_json", side_effect=fake_gh):
            result = fetch_comments.fetch_all("upstream", "project", 42)

        self.assertEqual(nested_cursors, [100, 200])
        self.assertEqual(result["review_threads"], [
            {"id": "long-thread", "isResolved": False, "comments": {"nodes": comments}},
            {"id": "short-thread", "isResolved": True,
             "comments": {"nodes": [{"id": "only-comment"}]}},
        ])
        self.assertEqual(set(result), {"pull_request", "conversation_comments", "reviews", "review_threads"})


if __name__ == "__main__":
    unittest.main()
