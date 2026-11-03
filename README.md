# Personal agent skills

Reusable skills maintained by [Saul Shanabrook](https://github.com/saulshanabrook).
Each skill is a folder containing `SKILL.md` and any supporting scripts or references.

## Install a linked copy

Clone the collection, then link the skills you want into your agent's personal skill directory:

```sh
git clone --recurse-submodules https://github.com/saulshanabrook/skills.git ~/p/skills
python3 ~/p/skills/scripts/skills.py install respond-to-review
```

Omit the skill name to install the whole collection. The default destination is
`~/.agents/skills`, which [Codex discovers, including symlinked skill folders](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).
Use `--dest PATH` for another compatible agent's skill directory.
The installer preserves existing installations: matching links are left alone,
and a conflicting file or directory is reported rather than overwritten.

The link points to the whole folder, so scripts and references stay available.
Edits in this checkout are immediately reflected in the installed skill.
Codex detects updates automatically; restart it if an update is missed.

To get published updates:

```sh
git -C ~/p/skills pull --ff-only
git -C ~/p/skills submodule update --init --recursive
```

Run `install` again to link any newly added skills you want. A pull that cannot
fast-forward leaves local work for you to reconcile.

## Available skills

| Skill | Purpose |
| --- | --- |
| [respond-to-review](respond-to-review/SKILL.md) | Retrieve GitHub review threads and investigate feedback through questions, evidence, changes, and concise replies. |
| [github-pr-worktree-checkout](github-pr-worktree-checkout/SKILL.md) | Reuse or create an isolated checkout for a GitHub PR; includes its Fish helper. |
| [github-actions-rest-logs](github-actions-rest-logs/SKILL.md) | Retrieve Actions runs, jobs, and logs using authenticated `gh`. |
| [git-diff-convention-sync](git-diff-convention-sync/SKILL.md) | Carry conventions from an accepted diff into project guidance. |
| [review-diff-reduction](review-diff-reduction/SKILL.md) | Reduce incidental changes in an existing diff. |
| [scientific-method-debugging](scientific-method-debugging/SKILL.md) | Investigate competing explanations with discriminating probes. |
| [primary-source-spec-refactor](primary-source-spec-refactor/SKILL.md) | Restructure technical specifications using primary evidence. |
| [refactor-python-package](refactor-python-package/SKILL.md) | Review and improve Python package boundaries. |
| [visualization-design-review](visualization-design-review/SKILL.md) | Design or critique visualizations around reader tasks and evidence. |
| [jupyter-notebook](jupyter-notebook/SKILL.md) | Create and revise notebooks with appropriate templates. |
| [sociocracy](sociocracy/SKILL.md) | Coordinate bounded agent roles, decisions, and handoffs. |

`gh-address-comments` has been merged into `respond-to-review`, including its
GitHub comment collector. If you installed the old skill through a symlink,
remove that old link and install `respond-to-review` instead.

Individual skills describe their prerequisites. GitHub skills generally need Git
and authenticated `gh`; the worktree helper additionally needs Fish. The
collection manager itself needs only Python 3 and Git. Existing license files
are retained with the skills they cover.

## Edit and publish

Edit the files in the checkout. Review the diff, validate the affected skill,
and exercise changed scripts before publishing. To commit one or more skill
folders and push them to this repository:

```sh
python3 ~/p/skills/scripts/skills.py publish respond-to-review -m "Clarify review response guidance"
```

This stages only the named skill folders, rejects unrelated files already in
the index, checks whitespace, commits changes, and runs a normal Git push.
Unrelated unstaged files remain untouched. If pushing fails, the commit stays
local; run the same command again to retry. It never force-pushes. As with any
Git push, earlier unpublished commits on the branch are published too.

For collection-level files such as this README or the manager, use ordinary
Git commands with the specific paths belonging to that change. Test the manager
with:

```sh
python3 -B -m unittest discover -s scripts -p test_skills.py -v
```

### This computer

Saul's existing checkout is `~/.codex/skills`; `~/p/skills` is an alias to that
same directory. Those skills are already installed here, so there is no second
copy to synchronize. Local agent instructions route future personal-skill edits
to this checkout and publish completed changes unless the request is private,
draft-only, or read-only. Repository history is the shared version; linked
folders are how other installations use it.

Bundled system skills and plugin-installed skills are maintained separately and
are not imported into this collection.
