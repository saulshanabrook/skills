#!/usr/bin/env python3
"""Link skills from this checkout or commit and push selected skill changes."""

import argparse
import re
import subprocess
import sys
from pathlib import Path


def git(root, *arguments):
    """Keep Git failures readable without hiding its diagnostic output."""
    result = subprocess.run(
        ["git", "-C", str(root), *arguments],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="surrogateescape",
    )
    if result.returncode:
        detail = (result.stderr + result.stdout).strip()
        raise RuntimeError(f"git {arguments[0]} failed:\n{detail}")
    if result.stderr:
        print(result.stderr, file=sys.stderr, end="")
    return result.stdout


def select_skills(root, names):
    """Accept only named skill directories directly inside this checkout."""
    selected = []
    for name in dict.fromkeys(names):
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
            raise RuntimeError(f"invalid skill name: {name!r}")
        source = root / name
        if source.is_symlink() or not (source / "SKILL.md").is_file():
            raise RuntimeError(f"not a skill directory: {name}")
        selected.append(source)
    return selected


def install(root, names, destination):
    if not names:
        names = sorted(
            entry.name for entry in root.iterdir()
            if entry.is_dir() and (entry / "SKILL.md").is_file()
        )
    sources = select_skills(root, names)
    destination = destination.expanduser().absolute()
    missing = []
    for source in sources:
        target = destination / source.name
        if target.exists() or target.is_symlink():
            try:
                if target.samefile(source):
                    continue
            except OSError:
                pass
            raise RuntimeError(f"refusing to overwrite {target}")
        missing.append((source, target))
    if missing:
        destination.mkdir(parents=True, exist_ok=True)
    for source, target in missing:
        target.symlink_to(source, target_is_directory=True)
        print(f"Linked {target} -> {source}")
    if not missing:
        print("Skills already installed." if sources else "No skills found.")


def publish(root, names, message):
    sources = select_skills(root, names)
    prefixes = tuple(source.name + "/" for source in sources)
    staged = git(root, "diff", "--cached", "--name-only", "--no-renames", "-z")
    unrelated = [name for name in staged.split("\0") if name and not name.startswith(prefixes)]
    if unrelated:
        raise RuntimeError("unrelated files are already staged:\n" + "\n".join(unrelated))
    git(root, "add", "--all", "--", *(source.name for source in sources))
    git(root, "diff", "--cached", "--check")
    if git(root, "diff", "--cached", "--name-only", "-z"):
        print(git(root, "commit", "-m", message), end="")
    else:
        print("No selected changes to commit; pushing HEAD.")
    print(git(root, "push", "origin", "HEAD"), end="")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    installer = commands.add_parser("install", help="link skill folders into an agent skills directory")
    installer.add_argument("skills", nargs="*", help="skill names; defaults to every skill in this checkout")
    installer.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills")
    publisher = commands.add_parser("publish", help="commit selected skill folders and push origin HEAD")
    publisher.add_argument("skills", nargs="+", help="skill names to publish")
    publisher.add_argument("-m", "--message", required=True, help="commit message")
    arguments = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    try:
        if arguments.command == "install":
            install(root, arguments.skills, arguments.dest)
        else:
            publish(root, arguments.skills, arguments.message)
    except (OSError, RuntimeError) as error:
        parser.exit(1, f"error: {error}\n")


if __name__ == "__main__":
    main()
