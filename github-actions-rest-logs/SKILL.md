---
name: github-actions-rest-logs
description: Use when a user wants GitHub Actions runs, jobs, or raw job logs fetched through an authenticated GitHub CLI session, especially when MCP or the web UI does not expose enough detail to diagnose a failing workflow.
---

# GitHub Actions REST Logs

Use this skill when:

- a user asks for the latest GitHub Actions run or failing job logs
- you need raw job logs rather than summary status
- the GitHub CLI is authenticated for the target repository

## Workflow

1. Determine the repo from `git remote get-url origin` unless the user gave `owner/repo`.
2. Confirm keychain-backed CLI authentication with `gh auth status --hostname github.com`; use `gh auth login` if needed.
3. List recent runs and pick the latest relevant run with the bundled helper.
4. List jobs for the selected run, then download logs for the failed jobs.
5. Use `gh api` for any endpoint the helper does not cover. Do not persist a GitHub token in shell configuration.
6. Summarize the actionable failure, not just the final GitHub wrapper error.

## Preferred commands

- Use `scripts/fetch_logs.sh list-runs owner/repo` to list recent runs.
- Use `scripts/fetch_logs.sh list-jobs owner/repo RUN_ID` to list jobs in a run.
- Use `scripts/fetch_logs.sh failed-logs owner/repo RUN_ID` to download all failed job logs for one run.

## Diagnosis guidance

- Prefer the newest failed CI run on the current branch or PR unless the user points to a different run.
- If GitHub returns `410 Gone`, the retained logs have expired; report that boundary and use a newer run or reproduce locally.
- For workflow command strings, inspect quoting carefully. GitHub Actions wrappers often add their own shell quoting.
- When a job fails before tests run, look for argument parsing errors, missing files, bad selectors, or shell escaping before changing product code.
- Quote URLs in `zsh` when they contain `?`.

## Output expectations

- Report the run ID, failing jobs, and the first actionable root cause.
- Include exact job IDs when useful for follow-up.
- If the failure is in workflow configuration rather than repo code, say so directly and patch the workflow.
