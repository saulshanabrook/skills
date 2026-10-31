#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  fetch_logs.sh list-runs OWNER/REPO
  fetch_logs.sh list-jobs OWNER/REPO RUN_ID
  fetch_logs.sh download-log OWNER/REPO JOB_ID [OUTFILE]
  fetch_logs.sh failed-logs OWNER/REPO RUN_ID [OUTDIR]

Requires:
  authenticated gh CLI
  jq
EOF
}

if [[ $# -lt 2 ]]; then
  usage
  exit 1
fi

for required_command in gh jq; do
  if ! command -v "$required_command" >/dev/null 2>&1; then
    printf 'Required command not found: %s\n' "$required_command" >&2
    exit 1
  fi
done

if ! gh auth status --hostname github.com >/dev/null 2>&1; then
  printf '%s\n' 'GitHub CLI is not authenticated; run: gh auth login' >&2
  exit 1
fi

mode="$1"
repo="$2"
api="repos/$repo/actions"

case "$mode" in
  list-runs)
    gh api "$api/runs?per_page=${PER_PAGE:-10}" \
      | jq '.workflow_runs[] | {id, name, head_branch, head_sha, event, status, conclusion, created_at, updated_at, html_url}'
    ;;
  list-jobs)
    run_id="${3:?RUN_ID required}"
    gh api "$api/runs/$run_id/jobs?per_page=100" \
      | jq '.jobs[] | {id, name, status, conclusion, started_at, completed_at, html_url}'
    ;;
  download-log)
    job_id="${3:?JOB_ID required}"
    outfile="${4:-job-${job_id}.log}"
    gh api --allow-escape-sequences "$api/jobs/$job_id/logs" > "$outfile"
    printf '%s\n' "$outfile"
    ;;
  failed-logs)
    run_id="${3:?RUN_ID required}"
    outdir="${4:-./gh-action-logs-$run_id}"
    mkdir -p "$outdir"
    jobs_json="$outdir/jobs.json"
    gh api "$api/runs/$run_id/jobs?per_page=100" > "$jobs_json"
    jq '.jobs[] | {id, name, status, conclusion, html_url}' "$jobs_json"
    jq -r '.jobs[] | select(.conclusion == "failure") | [.id, .name] | @tsv' "$jobs_json" \
      | while IFS=$'\t' read -r job_id job_name; do
          safe_name="$(printf '%s' "$job_name" | tr ' /()' '____')"
          outfile="$outdir/${job_id}-${safe_name}.log"
          gh api --allow-escape-sequences "$api/jobs/$job_id/logs" > "$outfile"
          printf '%s\t%s\n' "$job_name" "$outfile"
        done
    ;;
  *)
    usage
    exit 1
    ;;
esac
