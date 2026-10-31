function __prwt_remote_slug --description 'Normalize a Git remote to its owner/repository slug'
    set -l remote_name "$argv[1]"
    set -l current_repo_slug "$argv[2]"

    if test "$remote_name" = .
        string lower -- "$current_repo_slug"
        return 0
    end

    set -l remote_url (git remote get-url "$remote_name" 2>/dev/null)
    if test $status -ne 0; or test -z "$remote_url"
        return 1
    end

    set -l remote_slug (string replace -r '\.git/?$' '' -- "$remote_url")
    set remote_slug (string replace -r '^[^/@:]+@[^/:]+:' '' -- "$remote_slug")
    set remote_slug (string replace -r '^[A-Za-z][A-Za-z0-9+.-]*://([^/@]+@)?[^/]+/' '' -- "$remote_slug")
    set remote_slug (string trim -c / -- "$remote_slug")
    string lower -- "$remote_slug"
end

function prwt --description 'Open or reuse a GitHub pull request worktree'
    if test (count $argv) -ne 1
        echo 'usage: prwt <pr-number|pr-url|head-branch>' >&2
        return 2
    end

    if not command -q git; or not command -q gh
        echo 'prwt: both git and gh are required' >&2
        return 127
    end

    set -l repo_root (git rev-parse --show-toplevel 2>/dev/null)
    if test $status -ne 0
        echo 'prwt: run this command from inside a Git repository' >&2
        return 2
    end

    set -l repo_slug (gh repo view --json nameWithOwner --jq .nameWithOwner 2>/dev/null)
    if test $status -ne 0; or test -z "$repo_slug"
        echo 'prwt: could not identify the current GitHub repository' >&2
        return 1
    end

    set -l pr_line (gh pr view "$argv[1]" --json number,headRefName,headRefOid,headRepository,url \
        --jq '[.number, .headRefName, .headRefOid, (.headRepository.nameWithOwner // ""), .url] | @tsv' 2>/dev/null)
    if test $status -ne 0; or test -z "$pr_line"
        echo "prwt: could not resolve pull request '$argv[1]' in $repo_slug" >&2
        return 1
    end

    set -l pr_fields (string split \t -- "$pr_line")
    if test (count $pr_fields) -ne 5
        echo 'prwt: GitHub returned unexpected pull request metadata' >&2
        return 1
    end

    set -l pr_number $pr_fields[1]
    set -l head_ref $pr_fields[2]
    set -l head_oid $pr_fields[3]
    set -l head_repo_slug $pr_fields[4]
    set -l pr_url $pr_fields[5]
    set -l repo_name (string split -r -m 1 / -- "$repo_slug")[-1]
    set -l path_slug (string replace -ar '[^A-Za-z0-9._-]+' '-' -- "$head_ref")
    set path_slug (string trim -c - -- "$path_slug")
    if test -z "$path_slug"
        set path_slug pr$pr_number
    end

    set -l worktree_root "$HOME/p/wt"
    if set -q PRWT_ROOT; and test -n "$PRWT_ROOT"
        set worktree_root "$PRWT_ROOT"
    end
    mkdir -p "$worktree_root"; or return
    set worktree_root (realpath "$worktree_root")
    set -l worktree_path "$worktree_root/$repo_name/pr$pr_number-$path_slug"
    set -l local_branch "pr-$pr_number-$path_slug"
    set -l pr_ref "refs/prwt/$pr_number"

    set -l base_remote
    for remote in (git remote)
        set -l remote_slug (__prwt_remote_slug "$remote" "$repo_slug")
        if test "$remote_slug" = (string lower -- "$repo_slug")
            set base_remote "$remote"
            break
        end
    end
    if test -z "$base_remote"; and git remote get-url origin >/dev/null 2>&1
        set base_remote origin
    end
    if test -z "$base_remote"
        set base_remote (git remote | head -n 1)
    end
    if test -z "$base_remote"
        echo 'prwt: the current repository has no Git remote' >&2
        return 1
    end

    echo "Fetching PR #$pr_number from $base_remote..." >&2
    if not git fetch --no-tags "$base_remote" "+refs/pull/$pr_number/head:$pr_ref"
        echo "prwt: failed to fetch $pr_url" >&2
        return 1
    end

    # Prefer a local branch whose upstream is the PR's actual head repository
    # and ref. A same-named local branch is a useful fallback for branches that
    # predate upstream configuration; the generated pr-* branch remains last.
    set -l repo_root (realpath "$repo_root")
    set -l matching_branches
    set -l matching_worktrees
    set -l named_branch
    set -l named_worktree
    set -l expected_upstream_ref "refs/heads/$head_ref"
    set -l expected_head_repo (string lower -- "$head_repo_slug")

    for branch_line in (git for-each-ref \
            --format='%(refname:short)%09%(upstream:remotename)%09%(upstream:remoteref)%09%(worktreepath)' \
            refs/heads)
        set -l branch_fields (string split \t -- "$branch_line")
        if test (count $branch_fields) -ne 4
            continue
        end

        set -l branch_name $branch_fields[1]
        set -l upstream_remote $branch_fields[2]
        set -l upstream_ref $branch_fields[3]
        set -l branch_worktree $branch_fields[4]

        if test "$branch_name" = "$head_ref"
            set named_branch "$branch_name"
            set named_worktree "$branch_worktree"
        end

        if test -z "$expected_head_repo"; or test "$upstream_ref" != "$expected_upstream_ref"
            continue
        end

        set -l upstream_repo (__prwt_remote_slug "$upstream_remote" "$repo_slug")
        if test "$upstream_repo" = "$expected_head_repo"
            set -a matching_branches "$branch_name"
            set -a matching_worktrees "$branch_worktree"
        end
    end

    set -l reuse_branch
    set -l reuse_worktree

    # If prwt is run from a matching checkout, keep the user there.
    if test (count $matching_branches) -gt 0
        for index in (seq (count $matching_branches))
            if test -n "$matching_worktrees[$index]"; and test -d "$matching_worktrees[$index]"
                set -l candidate_root (realpath "$matching_worktrees[$index]")
                if test "$candidate_root" = "$repo_root"
                    set reuse_branch "$matching_branches[$index]"
                    set reuse_worktree "$matching_worktrees[$index]"
                    break
                end
            end
        end
    end

    # Otherwise prefer the PR's own branch name, then any checked-out matching
    # branch, then an unbound matching branch.
    if test -z "$reuse_branch"; and test (count $matching_branches) -gt 0
        for index in (seq (count $matching_branches))
            if test "$matching_branches[$index]" = "$head_ref"; and test -n "$matching_worktrees[$index]"
                set reuse_branch "$matching_branches[$index]"
                set reuse_worktree "$matching_worktrees[$index]"
                break
            end
        end
    end
    if test -z "$reuse_branch"; and test (count $matching_branches) -gt 0
        for index in (seq (count $matching_branches))
            if test -n "$matching_worktrees[$index]"
                set reuse_branch "$matching_branches[$index]"
                set reuse_worktree "$matching_worktrees[$index]"
                break
            end
        end
    end
    if test -z "$reuse_branch"; and test (count $matching_branches) -gt 0
        for index in (seq (count $matching_branches))
            if test "$matching_branches[$index]" = "$head_ref"
                set reuse_branch "$matching_branches[$index]"
                set reuse_worktree "$matching_worktrees[$index]"
                break
            end
        end
    end
    if test -z "$reuse_branch"; and test (count $matching_branches) -gt 0
        set reuse_branch "$matching_branches[1]"
        set reuse_worktree "$matching_worktrees[1]"
    end
    if test -z "$reuse_branch"; and test -n "$named_branch"
        set reuse_branch "$named_branch"
        set reuse_worktree "$named_worktree"
    end
    if test -z "$reuse_branch"; and git show-ref --verify --quiet "refs/heads/$local_branch"
        set reuse_branch "$local_branch"
        for branch_line in (git for-each-ref \
                --format='%(refname:short)%09%(worktreepath)' "refs/heads/$local_branch")
            set -l branch_fields (string split \t -- "$branch_line")
            if test (count $branch_fields) -eq 2
                set reuse_worktree "$branch_fields[2]"
            end
        end
    end

    if test -n "$reuse_worktree"
        if not test -d "$reuse_worktree"
            echo "prwt: matching branch $reuse_branch is registered to a missing worktree; leaving it unchanged" >&2
            echo "Worktree: $reuse_worktree" >&2
            return 2
        end

        set -l current_oid (git -C "$reuse_worktree" rev-parse HEAD 2>/dev/null)
        if test -z "$current_oid"
            echo "prwt: could not inspect the existing $reuse_branch worktree; leaving it unchanged" >&2
            echo "Worktree: $reuse_worktree" >&2
            return 2
        end
        if test "$current_oid" != "$head_oid"
            set -l worktree_status (git -C "$reuse_worktree" status --porcelain)
            if test -z "$worktree_status"; and git merge-base --is-ancestor "$current_oid" "$pr_ref"
                git -C "$reuse_worktree" merge --ff-only "$pr_ref"; or return
            else
                echo 'prwt: existing worktree is not at the current PR head; leaving it unchanged' >&2
                echo "Branch: $reuse_branch" >&2
                echo "Worktree: $reuse_worktree" >&2
                cd "$reuse_worktree"
                return 2
            end
        end
        cd "$reuse_worktree"
        echo "$pr_url"
        echo "Branch: $reuse_branch"
        echo "Worktree: $reuse_worktree"
        return 0
    end

    if test -e "$worktree_path"
        echo "prwt: destination already exists but is not the $local_branch worktree:" >&2
        echo "  $worktree_path" >&2
        return 1
    end

    mkdir -p (dirname "$worktree_path"); or return
    if test -n "$reuse_branch"
        set -l branch_oid (git rev-parse "refs/heads/$reuse_branch")
        if test "$branch_oid" != "$head_oid"
            if git merge-base --is-ancestor "$branch_oid" "$pr_ref"
                git branch -f "$reuse_branch" "$pr_ref"; or return
            else
                echo "prwt: local branch $reuse_branch has diverged; leaving it unchanged" >&2
                return 2
            end
        end
        git worktree add "$worktree_path" "$reuse_branch"; or return
    else
        git worktree add -b "$local_branch" "$worktree_path" "$pr_ref"; or return
        set reuse_branch "$local_branch"
    end

    cd "$worktree_path"
    echo "$pr_url"
    echo "Branch: $reuse_branch"
    echo "Worktree: $worktree_path"
end
