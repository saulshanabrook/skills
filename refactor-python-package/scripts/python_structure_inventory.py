#!/usr/bin/env python3
"""Inventory structural signals in a Python source tree.

This is a conservative, standard-library-only aid for architecture review. It
does not decide whether a module is well designed, and its static import graph
cannot see dynamic imports, plugin loading, or every conditional import.
"""

from __future__ import annotations

import argparse
import ast
from collections import defaultdict
from dataclasses import asdict, dataclass, field
import json
from pathlib import Path
import sys
import tokenize
from typing import Iterable


EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pytest_cache",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "env",
    "node_modules",
    "site-packages",
    "venv",
}
TEST_DIRS = {"test", "tests", "testing"}


@dataclass
class RawImport:
    module: str | None
    level: int
    names: list[str]


@dataclass
class ModuleInfo:
    module: str
    path: str
    is_package: bool
    physical_lines: int
    code_lines: int
    public_names: list[str] = field(default_factory=list)
    declared_all: list[str] | None = None
    imports: list[str] = field(default_factory=list)
    internal_imports: list[str] = field(default_factory=list)
    fan_in: int = 0
    fan_out: int = 0
    identity_collision: bool = False
    parse_error: str | None = None
    _raw_imports: list[RawImport] = field(default_factory=list, repr=False)

    def serializable(self) -> dict[str, object]:
        result = asdict(self)
        result.pop("_raw_imports", None)
        return result


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Inventory Python modules, static imports, dependency cycles, and "
            "public top-level names. Results are review hints, not design verdicts."
        )
    )
    parser.add_argument("target", type=Path, help="Project, src, package, or .py path")
    parser.add_argument(
        "--json", action="store_true", help="Emit complete machine-readable JSON"
    )
    parser.add_argument(
        "--source-root",
        type=Path,
        help=(
            "Explicit module-name root. Use for namespace packages or when "
            "automatic src/project-root inference is ambiguous."
        ),
    )
    parser.add_argument(
        "--include-tests",
        action="store_true",
        help="Do not exclude tests found under the selected source roots",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=30,
        help="Maximum modules in the human-readable size table (default: 30)",
    )
    return parser.parse_args(argv)


def has_python_files(path: Path) -> bool:
    try:
        return any(path.rglob("*.py"))
    except OSError:
        return False


def choose_scope(
    target: Path, source_root_override: Path | None = None
) -> tuple[Path, list[Path]]:
    """Return the module-name root and source roots to scan."""
    target = target.resolve()
    if not target.exists():
        raise ValueError(f"target does not exist: {target}")
    if target.is_file() and target.suffix != ".py":
        raise ValueError(f"target file is not Python source: {target}")

    if source_root_override is not None:
        source_root = source_root_override.resolve()
        if not source_root.is_dir():
            raise ValueError(f"source root does not exist: {source_root}")
        try:
            target.relative_to(source_root)
        except ValueError as error:
            raise ValueError(
                f"target {target} is not inside source root {source_root}"
            ) from error
        return source_root, [target]

    if target.is_file():
        return target.parent, [target]

    if not target.is_dir():
        raise ValueError(f"target is not a file or directory: {target}")

    src = target / "src"
    if src.is_dir() and has_python_files(src):
        return src, [src]

    if target.name == "src" and has_python_files(target):
        return target, [target]

    if (target / "__init__.py").is_file():
        return target.parent, [target]

    return target, [target]


def should_exclude(path: Path, source_root: Path, include_tests: bool) -> bool:
    try:
        relative = path.relative_to(source_root)
    except ValueError:
        relative = path
    parts = set(relative.parts[:-1])
    if parts & EXCLUDED_DIRS:
        return True
    if not include_tests and (parts & TEST_DIRS or path.name.startswith("test_")):
        return True
    return False


def iter_python_files(
    roots: Iterable[Path], source_root: Path, include_tests: bool
) -> list[Path]:
    files: set[Path] = set()
    for root in roots:
        candidates = [root] if root.is_file() else root.rglob("*.py")
        for path in candidates:
            if not should_exclude(path, source_root, include_tests):
                files.add(path.resolve())
    return sorted(files)


def module_name(path: Path, source_root: Path) -> tuple[str, bool]:
    relative = path.relative_to(source_root)
    is_package = relative.name == "__init__.py"
    parts = list(relative.parts)
    if is_package:
        parts.pop()
    else:
        parts[-1] = Path(parts[-1]).stem
    if not parts:
        return source_root.name, True
    return ".".join(parts), is_package


def literal_all(node: ast.AST) -> list[str] | None:
    if not isinstance(node, (ast.List, ast.Tuple)):
        return None
    values: list[str] = []
    for item in node.elts:
        if not isinstance(item, ast.Constant) or not isinstance(item.value, str):
            return None
        values.append(item.value)
    return values


def assigned_names(node: ast.Assign | ast.AnnAssign) -> list[str]:
    targets = node.targets if isinstance(node, ast.Assign) else [node.target]
    names: list[str] = []
    for target in targets:
        if isinstance(target, ast.Name):
            names.append(target.id)
        elif isinstance(target, (ast.Tuple, ast.List)):
            names.extend(
                item.id for item in target.elts if isinstance(item, ast.Name)
            )
    return names


def analyze_file(path: Path, source_root: Path) -> ModuleInfo:
    module, is_package = module_name(path, source_root)
    try:
        with tokenize.open(path) as source:
            text = source.read()
    except (OSError, SyntaxError, UnicodeError) as error:
        return ModuleInfo(
            module=module,
            path=str(path),
            is_package=is_package,
            physical_lines=0,
            code_lines=0,
            parse_error=f"{type(error).__name__}: {error}",
        )
    lines = text.splitlines()
    info = ModuleInfo(
        module=module,
        path=str(path),
        is_package=is_package,
        physical_lines=len(lines),
        code_lines=sum(
            1 for line in lines if line.strip() and not line.lstrip().startswith("#")
        ),
    )

    try:
        tree = ast.parse(text, filename=str(path))
    except (SyntaxError, ValueError) as error:
        info.parse_error = f"{type(error).__name__}: {error}"
        return info

    public: set[str] = set()
    declared_all: list[str] | None = None
    imports: set[str] = set()
    raw_imports: list[RawImport] = []

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if not node.name.startswith("_"):
                public.add(node.name)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            names = assigned_names(node)
            public.update(name for name in names if not name.startswith("_"))
            value = node.value
            if "__all__" in names and value is not None:
                declared_all = literal_all(value)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = [alias.name for alias in node.names]
            imports.update(names)
            raw_imports.append(RawImport(module=None, level=0, names=names))
        elif isinstance(node, ast.ImportFrom):
            rendered = "." * node.level + (node.module or "")
            imports.add(rendered or "." * node.level)
            raw_imports.append(
                RawImport(
                    module=node.module,
                    level=node.level,
                    names=[alias.name for alias in node.names if alias.name != "*"],
                )
            )

    info.public_names = sorted(set(declared_all) if declared_all is not None else public)
    info.declared_all = declared_all
    info.imports = sorted(imports)
    info._raw_imports = raw_imports
    return info


def package_for(info: ModuleInfo) -> str:
    if info.is_package:
        return info.module
    return info.module.rpartition(".")[0]


def relative_base(info: ModuleInfo, raw: RawImport) -> str:
    package_parts = [part for part in package_for(info).split(".") if part]
    remove = max(raw.level - 1, 0)
    if remove:
        package_parts = package_parts[:-remove] if remove <= len(package_parts) else []
    if raw.module:
        package_parts.extend(raw.module.split("."))
    return ".".join(package_parts)


def nearest_module(candidate: str, modules: set[str]) -> str | None:
    current = candidate
    while current:
        if current in modules:
            return current
        current = current.rpartition(".")[0]
    return None


def resolve_internal_imports(info: ModuleInfo, modules: set[str]) -> set[str]:
    resolved: set[str] = set()
    for raw in info._raw_imports:
        if raw.level:
            base = relative_base(info, raw)
            candidates = [f"{base}.{name}" if base else name for name in raw.names]
            if raw.module:
                candidates.insert(0, base)
        elif raw.module is None:
            candidates = raw.names
        else:
            base = raw.module
            candidates = [f"{base}.{name}" for name in raw.names]
            candidates.append(base)

        for candidate in candidates:
            match = nearest_module(candidate, modules)
            if match and match != info.module:
                resolved.add(match)
    return resolved


def strongly_connected_components(
    graph: dict[str, set[str]],
) -> list[list[str]]:
    """Find SCCs with iterative Kosaraju traversal to avoid recursion limits."""
    visited: set[str] = set()
    finish_order: list[str] = []
    for start in sorted(graph):
        if start in visited:
            continue
        stack: list[tuple[str, bool]] = [(start, False)]
        while stack:
            node, expanded = stack.pop()
            if expanded:
                finish_order.append(node)
                continue
            if node in visited:
                continue
            visited.add(node)
            stack.append((node, True))
            for neighbor in sorted(graph.get(node, set()), reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, False))

    reverse_graph: dict[str, set[str]] = {node: set() for node in graph}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor in reverse_graph:
                reverse_graph[neighbor].add(node)

    assigned: set[str] = set()
    components: list[list[str]] = []
    for start in reversed(finish_order):
        if start in assigned:
            continue
        component: list[str] = []
        stack = [(start, False)]
        assigned.add(start)
        while stack:
            node, _ = stack.pop()
            component.append(node)
            for neighbor in reverse_graph.get(node, set()):
                if neighbor not in assigned:
                    assigned.add(neighbor)
                    stack.append((neighbor, False))
        components.append(sorted(component))

    return sorted(
        (component for component in components if len(component) > 1),
        key=lambda component: (-len(component), component),
    )


def build_inventory(
    target: Path, include_tests: bool, source_root_override: Path | None = None
) -> dict[str, object]:
    source_root, scan_roots = choose_scope(target, source_root_override)
    files = iter_python_files(scan_roots, source_root, include_tests)
    infos = [analyze_file(path, source_root) for path in files]

    infos_by_module: dict[str, list[ModuleInfo]] = defaultdict(list)
    for info in infos:
        infos_by_module[info.module].append(info)
    collision_names = {
        module for module, members in infos_by_module.items() if len(members) > 1
    }
    for module in collision_names:
        for info in infos_by_module[module]:
            info.identity_collision = True

    graph_infos = [info for info in infos if not info.identity_collision]
    module_set = {info.module for info in graph_infos}

    graph: dict[str, set[str]] = {}
    inbound: dict[str, set[str]] = defaultdict(set)
    for info in graph_infos:
        outgoing = resolve_internal_imports(info, module_set)
        graph[info.module] = outgoing
        info.internal_imports = sorted(outgoing)
        info.fan_out = len(outgoing)
        for dependency in outgoing:
            inbound[dependency].add(info.module)

    for info in graph_infos:
        info.fan_in = len(inbound[info.module])

    cycles = strongly_connected_components(graph)
    parse_errors = [info.module for info in infos if info.parse_error]
    module_collisions = [
        {
            "module": module,
            "paths": sorted(info.path for info in infos_by_module[module]),
        }
        for module in sorted(collision_names)
    ]
    return {
        "target": str(target.resolve()),
        "source_root": str(source_root),
        "scan_roots": [str(path) for path in scan_roots],
        "limitations": (
            "Static AST inventory only; dynamic imports, plugin loading, generated "
            "modules, inferred namespace roots, and semantic cohesion require "
            "manual review. Use --source-root when module-name inference is ambiguous."
        ),
        "summary": {
            "modules": len(infos),
            "unique_module_names": len(infos_by_module),
            "physical_lines": sum(info.physical_lines for info in infos),
            "code_lines": sum(info.code_lines for info in infos),
            "internal_edges": sum(len(edges) for edges in graph.values()),
            "cycle_components": len(cycles),
            "module_collisions": len(module_collisions),
            "parse_errors": len(parse_errors),
        },
        "cycles": cycles,
        "module_collisions": module_collisions,
        "parse_error_modules": parse_errors,
        "modules": [info.serializable() for info in infos],
    }


def print_human(inventory: dict[str, object], limit: int) -> None:
    summary = inventory["summary"]
    assert isinstance(summary, dict)
    modules = inventory["modules"]
    assert isinstance(modules, list)
    cycles = inventory["cycles"]
    assert isinstance(cycles, list)

    def counted(value: object, noun: str) -> str:
        return f"{value} {noun}{'' if value == 1 else 's'}"

    print("Python structure inventory")
    print(f"Source root: {inventory['source_root']}")
    print(
        "Summary: "
        f"{counted(summary['modules'], 'module')}, "
        f"{summary['physical_lines']} physical lines, "
        f"{summary['code_lines']} nonblank/noncomment lines, "
        f"{counted(summary['internal_edges'], 'static internal edge')}, "
        f"{counted(summary['cycle_components'], 'cycle component')}, "
        f"{counted(summary['module_collisions'], 'module-name collision')}, "
        f"{counted(summary['parse_errors'], 'parse error')}"
    )
    print()
    print("Largest modules (review hints, not violations):")
    print(f"{'lines':>7} {'code':>7} {'public':>7} {'in':>4} {'out':>4}  module")
    ranked = sorted(
        modules,
        key=lambda module: (-int(module["physical_lines"]), str(module["module"])),
    )
    for module in ranked[: max(limit, 0)]:
        print(
            f"{module['physical_lines']:>7} {module['code_lines']:>7} "
            f"{len(module['public_names']):>7} {module['fan_in']:>4} "
            f"{module['fan_out']:>4}  {module['module']}"
        )
    if len(ranked) > max(limit, 0):
        print(f"... {len(ranked) - max(limit, 0)} more; use --json for all modules")

    print()
    if cycles:
        print("Strongly connected import components:")
        for component in cycles:
            print("- " + ", ".join(component))
    else:
        print("No multi-module cycles found in the static import graph.")

    errors = inventory["parse_error_modules"]
    assert isinstance(errors, list)
    if errors:
        print()
        print("Modules with parse errors: " + ", ".join(str(item) for item in errors))

    collisions = inventory["module_collisions"]
    assert isinstance(collisions, list)
    if collisions:
        print()
        print("Ambiguous module identities (excluded from graph metrics):")
        for collision in collisions:
            print(f"- {collision['module']}")
            for path in collision["paths"]:
                print(f"  - {path}")

    print()
    print(inventory["limitations"])


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    if args.limit < 0:
        print("error: --limit must be non-negative", file=sys.stderr)
        return 2
    try:
        inventory = build_inventory(
            args.target, args.include_tests, source_root_override=args.source_root
        )
    except (OSError, UnicodeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    if args.json:
        json.dump(inventory, sys.stdout, indent=2, sort_keys=True)
        print()
    else:
        print_human(inventory, args.limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
