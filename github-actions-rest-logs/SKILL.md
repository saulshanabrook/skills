---
name: github-actions-rest-logs
description: Use when a user wants GitHub Actions runs, jobs, or raw job logs fetched directly from the GitHub REST API with GITHUB_PAT_TOKEN, especially when MCP or the web UI does not expose enough detail to diagnose a failing workflow.
---

# GitHub Actions REST Logs

Use this skill when:

- a user asks for the latest GitHub Actions run or failing job logs
- you need raw job logs rather than summary status
- `GITHUB_PAT_TOKEN` is available in the environment

## Workflow

1. Determine the repo from `git remote get-url origin` unless the user gave `owner/repo`.
2. Confirm `GITHUB_PAT_TOKEN` is set before making API requests.
3. List recent runs and pick the latest relevant run:
   - `curl -sS -H "Authorization: Bearer $GITHUB_PAT_TOKEN" -H "Accept: application/vnd.github+json" "https://api.github.com/repos/$repo/actions/runs?per_page=10" | jq ...`
4. List jobs for the selected run:
   - `curl -sS ... "https://api.github.com/repos/$repo/actions/runs/$run_id/jobs?per_page=100" | jq ...`
5. Download logs for failed jobs with `curl -L` against `/actions/jobs/$job_id/logs`.
6. Summarize the actionable failure, not just the final GitHub wrapper error.

## Preferred commands

- Use `scripts/fetch_logs.sh list-runs owner/repo` to list recent runs.
- Use `scripts/fetch_logs.sh list-jobs owner/repo RUN_ID` to list jobs in a run.
- Use `scripts/fetch_logs.sh failed-logs owner/repo RUN_ID` to download all failed job logs for one run.

## Diagnosis guidance

- Prefer the newest failed CI run on the current branch or PR unless the user points to a different run.
- For workflow command strings, inspect quoting carefully. GitHub Actions wrappers often add their own shell quoting.
- When a job fails before tests run, look for argument parsing errors, missing files, bad selectors, or shell escaping before changing product code.
- Quote URLs in `zsh` when they contain `?`.

## Output expectations

- Report the run ID, failing jobs, and the first actionable root cause.
- Include exact job IDs when useful for follow-up.
- If the failure is in workflow configuration rather than repo code, say so directly and patch the workflow.
