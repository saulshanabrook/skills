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
  GITHUB_PAT_TOKEN
  jq
EOF
}

if [[ $# -lt 2 ]]; then
  usage
  exit 1
fi

: "${GITHUB_PAT_TOKEN:?GITHUB_PAT_TOKEN must be set}"

mode="$1"
repo="$2"
api="https://api.github.com/repos/$repo/actions"
headers=(
  -H "Authorization: Bearer $GITHUB_PAT_TOKEN"
  -H "Accept: application/vnd.github+json"
)

case "$mode" in
  list-runs)
    curl -sS "${headers[@]}" "$api/runs?per_page=${PER_PAGE:-10}" \
      | jq '.workflow_runs[] | {id, name, head_branch, head_sha, event, status, conclusion, created_at, updated_at, html_url}'
    ;;
  list-jobs)
    run_id="${3:?RUN_ID required}"
    curl -sS "${headers[@]}" "$api/runs/$run_id/jobs?per_page=100" \
      | jq '.jobs[] | {id, name, status, conclusion, started_at, completed_at, html_url}'
    ;;
  download-log)
    job_id="${3:?JOB_ID required}"
    outfile="${4:-job-${job_id}.log}"
    curl -L -sS "${headers[@]}" "$api/jobs/$job_id/logs" -o "$outfile"
    printf '%s\n' "$outfile"
    ;;
  failed-logs)
    run_id="${3:?RUN_ID required}"
    outdir="${4:-./gh-action-logs-$run_id}"
    mkdir -p "$outdir"
    jobs_json="$outdir/jobs.json"
    curl -sS "${headers[@]}" "$api/runs/$run_id/jobs?per_page=100" > "$jobs_json"
    jq '.jobs[] | {id, name, status, conclusion, html_url}' "$jobs_json"
    jq -r '.jobs[] | select(.conclusion == "failure") | [.id, .name] | @tsv' "$jobs_json" \
      | while IFS=$'\t' read -r job_id job_name; do
          safe_name="$(printf '%s' "$job_name" | tr ' /()' '____')"
          outfile="$outdir/${job_id}-${safe_name}.log"
          curl -L -sS "${headers[@]}" "$api/jobs/$job_id/logs" -o "$outfile"
          printf '%s\t%s\n' "$job_name" "$outfile"
        done
    ;;
  *)
    usage
    exit 1
    ;;
esac
