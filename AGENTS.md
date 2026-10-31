# Maintaining this skill collection

- Each top-level folder with `SKILL.md` is an independently installable skill.
  Keep its required scripts, examples, and references inside that folder;
  document external prerequisites and preserve applicable license files.
- Edit the source folders directly. Installed symlinks point here; do not
  maintain generated copies or commit caches, local configuration, bundled
  `.system` skills, or plugin-managed installations.
- Use skill-creator validation when available. Exercise changed executable
  helpers with focused checks. For manager changes, run
  `python3 -B -m unittest discover -s scripts -p test_skills.py -v`.
- Preserve unrelated work. When publishing is authorized, inspect the diff and
  use `python3 scripts/skills.py publish SKILL -m "Message"` for selected skill
  folders, or stage explicit paths for collection-level changes. A push also
  publishes earlier local commits on the branch; account for those in the task.
- Use normal pushes. If a push is rejected, retain the local commit and report
  or reconcile the actual conflict; do not reset or force-push to hide it.
