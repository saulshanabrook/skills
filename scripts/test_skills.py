"""Exercise the public CLI against disposable checkouts and local bare remotes."""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class SkillsTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.root = self.base / "checkout"
        (self.root / "scripts").mkdir(parents=True)
        self.script = self.root / "scripts" / "skills.py"
        shutil.copyfile(Path(__file__).with_name("skills.py"), self.script)
        for name in ("alpha", "beta"):
            (self.root / name / "assets").mkdir(parents=True)
            (self.root / name / "SKILL.md").write_text(f"{name}\n")
            (self.root / name / "assets" / "data.txt").write_text("whole folder\n")
        self.environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        self.environment.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0")
        self.git("init", "--quiet", "--initial-branch=main")
        self.git("config", "user.name", "Skills Test")
        self.git("config", "user.email", "skills-test@example.invalid")
        self.git("add", ".")
        self.git("commit", "--quiet", "-m", "Initial skills")
        self.initial_head = self.git("rev-parse", "HEAD").strip()
        self.remote = self.base / "origin.git"
        self.git("init", "--quiet", "--bare", str(self.remote))
        self.git("remote", "add", "origin", str(self.remote))
        self.git("push", "--quiet", "origin", "HEAD")

    def git(self, *arguments, root=None):
        result = subprocess.run(
            ["git", "-C", str(root or self.root), *arguments],
            capture_output=True, text=True, env=self.environment,
        )
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        return result.stdout

    def cli(self, *arguments, script=None):
        return subprocess.run(
            [sys.executable, str(script or self.script), *arguments],
            cwd=self.base, capture_output=True, text=True, env=self.environment,
        )

    def test_install_links_complete_folders_and_repeated_install_is_noop(self):
        destination = self.base / "installed"
        first = self.cli("install", "--dest", str(destination))
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(sorted(entry.name for entry in destination.iterdir()), ["alpha", "beta"])
        linked = destination / "alpha"
        self.assertTrue(linked.is_symlink())
        self.assertEqual((linked / "assets" / "data.txt").read_text(), "whole folder\n")
        original_inode = linked.lstat().st_ino
        second = self.cli("install", "alpha", "--dest", str(destination))
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(linked.lstat().st_ino, original_inode)

    def test_install_into_source_is_noop(self):
        result = self.cli("install", "--dest", str(self.root))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.root / "alpha").is_symlink())

    def test_install_preflights_all_conflicts_before_linking(self):
        destination = self.base / "installed"
        (destination / "beta").mkdir(parents=True)
        marker = destination / "beta" / "keep.txt"
        marker.write_text("untouched\n")
        result = self.cli("install", "alpha", "beta", "--dest", str(destination))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("refusing to overwrite", result.stderr)
        self.assertFalse((destination / "alpha").exists())
        self.assertEqual(marker.read_text(), "untouched\n")

    def test_install_refuses_different_files_and_broken_links(self):
        destination = self.base / "installed"
        destination.mkdir()
        target = destination / "alpha"
        target.write_text("keep\n")
        result = self.cli("install", "alpha", "--dest", str(destination))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(target.read_text(), "keep\n")
        target.unlink()
        target.symlink_to(self.base / "missing")
        result = self.cli("install", "alpha", "--dest", str(destination))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(target.readlink(), self.base / "missing")

    def test_install_rejects_missing_and_traversal_names(self):
        destination = self.base / "installed"
        for name in ("absent", "../alpha", "alpha/..", str(self.root / "alpha"), ".system"):
            with self.subTest(name=name):
                result = self.cli("install", name, "--dest", str(destination))
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(destination.exists())

    def test_script_resolves_checkout_through_a_directory_alias(self):
        alias = self.base / "alias"
        alias.symlink_to(self.root, target_is_directory=True)
        destination = self.base / "installed"
        result = self.cli("install", "alpha", "--dest", str(destination), script=alias / "scripts" / "skills.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((destination / "alpha").readlink(), (self.root / "alpha").resolve())

    def test_publish_commits_only_selected_skills_and_preserves_other_work(self):
        (self.root / "alpha" / "SKILL.md").write_text("alpha updated\n")
        (self.root / "beta" / "SKILL.md").write_text("beta still editing\n")
        (self.root / "scratch.txt").write_text("unrelated untracked file\n")
        result = self.cli("publish", "alpha", "-m", "Update alpha")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"), "alpha/SKILL.md\n")
        self.assertEqual(self.git("status", "--porcelain"), " M beta/SKILL.md\n?? scratch.txt\n")
        self.assertEqual(self.git("rev-parse", "HEAD"), self.git("rev-parse", "refs/heads/main", root=self.remote))

    def test_publish_rejects_unrelated_staging_before_changing_index(self):
        (self.root / "alpha" / "SKILL.md").write_text("alpha updated\n")
        (self.root / "beta" / "SKILL.md").write_text("beta updated\n")
        self.git("add", "beta")
        before = self.git("diff", "--cached", "--binary")
        result = self.cli("publish", "alpha", "-m", "Update alpha")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unrelated files are already staged", result.stderr)
        self.assertEqual(self.git("diff", "--cached", "--binary"), before)
        self.assertEqual(self.git("rev-parse", "HEAD").strip(), self.initial_head)

    def test_publish_allows_staged_selected_work(self):
        (self.root / "alpha" / "SKILL.md").write_text("alpha updated\n")
        self.git("add", "alpha")
        result = self.cli("publish", "alpha", "-m", "Update alpha")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_publish_includes_a_new_skill_folder(self):
        (self.root / "gamma").mkdir()
        (self.root / "gamma" / "SKILL.md").write_text("new skill\n")
        (self.root / "gamma" / "resource.txt").write_text("new resource\n")
        result = self.cli("publish", "gamma", "-m", "Add gamma")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"),
            "gamma/SKILL.md\ngamma/resource.txt\n",
        )
        self.assertEqual(self.git("rev-parse", "HEAD"), self.git("rev-parse", "refs/heads/main", root=self.remote))

    def test_publish_checks_whitespace_in_new_files_before_commit(self):
        (self.root / "alpha" / "new.txt").write_text("trailing whitespace \n")
        result = self.cli("publish", "alpha", "-m", "Invalid whitespace")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("trailing whitespace", result.stderr)
        self.assertEqual(self.git("rev-parse", "HEAD").strip(), self.initial_head)
        self.assertEqual(self.git("rev-parse", "refs/heads/main", root=self.remote).strip(), self.initial_head)

    def test_failed_push_can_be_retried_without_another_commit(self):
        (self.root / "alpha" / "SKILL.md").write_text("alpha updated\n")
        self.git("remote", "set-url", "origin", str(self.base / "unavailable.git"))
        first = self.cli("publish", "alpha", "-m", "Update alpha")
        self.assertNotEqual(first.returncode, 0)
        self.assertIn("git push failed", first.stderr)
        committed_head = self.git("rev-parse", "HEAD")
        self.assertNotEqual(committed_head.strip(), self.initial_head)
        self.assertEqual(self.git("status", "--porcelain"), "")
        self.git("remote", "set-url", "origin", str(self.remote))
        retry = self.cli("publish", "alpha", "-m", "Retry push")
        self.assertEqual(retry.returncode, 0, retry.stderr)
        self.assertEqual(self.git("rev-parse", "HEAD"), committed_head)
        self.assertEqual(self.git("rev-parse", "refs/heads/main", root=self.remote), committed_head)

    def test_publish_does_not_force_a_divergent_remote(self):
        other = self.base / "other"
        self.git("clone", "--quiet", "--branch=main", str(self.remote), str(other))
        self.git("config", "user.name", "Other Test", root=other)
        self.git("config", "user.email", "other@example.invalid", root=other)
        (other / "beta" / "SKILL.md").write_text("remote beta update\n")
        self.git("commit", "--quiet", "-am", "Remote beta update", root=other)
        self.git("push", "--quiet", "origin", "HEAD", root=other)
        remote_head = self.git("rev-parse", "HEAD", root=other)
        (self.root / "alpha" / "SKILL.md").write_text("local alpha update\n")
        result = self.cli("publish", "alpha", "-m", "Local alpha update")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("rejected", result.stderr)
        self.assertEqual(self.git("rev-parse", "refs/heads/main", root=self.remote), remote_head)
        self.assertNotEqual(self.git("rev-parse", "HEAD").strip(), self.initial_head)


if __name__ == "__main__":
    unittest.main()
