---
name: github-pr-worktree-checkout
description: Open or reuse a GitHub pull request in an existing matching local branch/worktree or a dedicated worktree under the repository-specific ~/p/wt directory. Use when the user asks Codex to check out, open, inspect, review, or work on a PR in a worktree, or when PR work should be isolated from the main checkout.
---

# GitHub PR Worktree Checkout

Use the Fish function `prwt` as the source of truth for worktree selection
and creation. Prefer an installed function; otherwise source the bundled
[scripts/prwt.fish](scripts/prwt.fish). This requires Fish, Git, and an
authenticated GitHub CLI (`gh`).

The function accepts a PR number, PR URL, or head-branch name,
fetches the PR head, finds a local branch tracking that exact head repository
and ref, and reuses its worktree safely. If no tracked branch exists, it checks
for a same-named local branch before creating a collision-resistant managed
branch.

## Open the PR

1. Start from any directory inside the intended repository.
2. Run `prwt <selector>` in Fish if the function is installed. Otherwise source
   `<skill-dir>/scripts/prwt.fish` first, where `<skill-dir>` is the directory
   containing this `SKILL.md`. From another shell, this command prefers an
   installed function and falls back to the bundled helper:

   ```bash
   fish -c 'functions -q prwt; or source "$argv[1]"; or exit $status; prwt "$argv[2]"; and pwd' '<skill-dir>/scripts/prwt.fish' <selector>
   ```

   Use the final path as the working directory for later commands. Set
   `PRWT_ROOT` to override the default `~/p/wt` worktree root.
3. Treat the path printed after `Worktree:` as authoritative. It can be an
   existing checkout anywhere on disk. A newly created checkout uses
   `~/p/wt/<repo>/pr<number>-<head-branch>`.
4. If `prwt` returns nonzero because an existing worktree is dirty, stale, or
   divergent, inspect it and report the condition. Do not reset, clean, or
   overwrite it without explicit user direction.

## Verify the Binding

Before editing or reviewing, pin the current state:

```bash
gh pr view <selector> --json number,url,headRefName,headRefOid
git -C <worktree> status --short --branch
git -C <worktree> rev-parse HEAD
git worktree list --porcelain
```

Require the local `HEAD` to equal `headRefOid` before treating the checkout as
the current PR head. Refresh this comparison after a force-push or when the
user asks for a re-review.

## Preserve Existing Work

- Prefer a branch whose upstream remote resolves to the PR head repository and
  whose upstream ref equals the PR head ref.
- Prefer an existing checkout of that branch; when several branches match,
  prefer the current checkout, then the same-named PR branch.
- If no upstream matches, reuse a same-named local branch, then an already-bound
  `pr-<number>-<slug>` managed branch.
- Allow `prwt` to fast-forward only a clean, non-divergent selected branch.
- Leave dirty, stale, or divergent branches and worktrees unchanged; do not
  create a duplicate managed worktree to bypass them.
- Keep unrelated checkouts untouched.
- Do not remove a worktree unless the user requests cleanup and it is clean.
