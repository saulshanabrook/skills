---
name: refactor-python-package
description: Review and refactor the organization of Python packages and applications. Use when Codex needs to assess or change module and package boundaries, split or merge Python modules, reduce circular imports or inappropriate coupling, establish dependency layers, reorganize a project into a src layout, clean up __init__.py or public exports, preserve stable import paths, investigate oversized or fragmented modules, or produce an evidence-backed package-structure review. Applies to .py source trees, pyproject.toml layouts, import graphs, and organization-focused code reviews; do not use for ordinary function-level cleanup with no module or package design question.
---

# Refactor Python Package

Organize code around cohesive concepts, useful interfaces, and intentional dependency direction. Treat line count as a smoke alarm, not the definition of a good boundary.

## Choose the outcome

Match the work to the user's authorization:

| Request | Outcome |
|---|---|
| Review, assess, diagnose, or suggest | Inspect read-only and return prioritized findings. Do not edit files. |
| Make a plan or handoff | Return a sequenced plan with proposed moves, compatibility strategy, risks, and verification. |
| Refactor, reorganize, split, merge, or fix | Establish a baseline, make the smallest coherent changes, and verify them. |
| Define a convention or policy | Recommend project-specific rules and tooling without adding dependencies or changing configuration unless asked. |

Do not infer permission to replace a public API, migrate the packaging layout, or add architecture tooling from a review-only request.

## Establish constraints

1. Read repository instructions and contributor documentation.
2. Inspect `pyproject.toml` and any build, lint, type-check, test, or documentation configuration.
3. Locate import-package roots, including `src/`, flat layouts, namespace packages, generated sources, vendored code, and native-extension boundaries.
4. Check working-tree state and preserve unrelated user changes.
5. Identify supported Python versions, frameworks, entry points, plugin systems, serialization formats, and documented public import paths.
6. Ask only when a missing choice would materially change compatibility or scope. Otherwise state the assumption and continue.

Treat repository layout and internal module design as separate questions. A `src/` migration can improve packaging correctness without improving cohesion, and a well-designed package can use either physical layout.

## Build an evidence baseline

Before recommending boundaries, collect enough evidence to understand the current system:

- Map source packages, subpackages, tests, examples, generated files, and entry points.
- Record module size, top-level public definitions, direct imports, cycles, fan-in, and fan-out.
- Inspect `__init__.py`, `__all__`, underscore-prefixed modules, re-exports, lazy imports, and module-level side effects.
- Search documentation, tests, examples, and downstream compatibility tests for supported import paths.
- Identify pure logic, stateful orchestration, I/O, framework integration, optional dependencies, and composition roots.
- Use version history when available to find files that change together, high-churn hotspots, and unrelated regions that evolve independently.
- Run the configured baseline tests, lint, type checks, or import smoke tests before editing when proportionate and feasible. Record pre-existing failures.

Run `scripts/python_structure_inventory.py <target>` from this skill directory, or resolve it relative to this `SKILL.md`, for a first-pass inventory. Add `--json` for machine-readable output. For a namespace package or ambiguous direct package path, pass `--source-root <import-root>` so dotted module names are derived correctly. Treat the AST-based results as structural hints: dynamic imports, generated modules, runtime plugin loading, and conditional imports require manual inspection.

Prefer repository-native commands and already configured tools. Do not install Pylint, Radon, Import Linter, pydeps, or other dependencies merely to complete a review.

## Evaluate module boundaries

Evaluate each candidate boundary across several dimensions rather than using one metric:

| Dimension | Questions |
|---|---|
| Responsibility | Can the module's purpose be stated precisely without joining unrelated jobs with “and”? |
| Cohesion | Do its definitions share vocabulary, invariants, state, callers, tests, and reasons to change? |
| Coupling | Which modules must know about its implementation? Are dependencies narrow and one-way? |
| Interface depth | Does a small, stable surface hide useful implementation, or do many shallow files merely forward calls? |
| Dependency character | Does one region use pure core dependencies while another requires network, storage, framework, or optional packages? |
| Public API | Are canonical import paths intentional, documented, and distinguishable from implementation paths? |
| Import behavior | Are there cycles, expensive imports, mutable globals, registration effects, or order-sensitive initialization? |
| Change evidence | Do separate regions change independently, or do many tiny modules always change together? |
| Testability | Can behavior be tested without unrelated fixtures or infrastructure? |

Keep code together when it enforces one concept or invariant, changes together, or provides private helpers behind a useful interface. Split when a subset has an independently nameable responsibility, dependency set, public status, test strategy, or change pattern.

Do not default to one class per file. Avoid both god modules and “ravioli” designs made of tiny mutually dependent files. Keep a helper beside its only caller until it has multiple real users and a meaningful home. Treat generic `utils.py`, `helpers.py`, and `common.py` modules as prompts to find a domain or capability name, not as automatic violations.

Start with a relatively flat package. Introduce a subpackage when it represents a stable namespace, an enforceable dependency boundary, an optional backend family, or a group of related modules that users navigate together. Do not create directory depth solely to reduce file length.

For applications, choose domain-first or layer-first organization based on real change and dependency boundaries. For libraries and compiler-like pipelines, organize around public concepts, intermediate representations, transformations, and adapters while keeping core types independent of parsers, CLIs, databases, and frameworks.

## Interpret size and metrics

Use no universal line-count rule. For hand-written logic, a local policy may use roughly 500–600 lines as a soft review prompt and Pylint's 1,000-line default as an upper warning. Label both as heuristics, not Python standards or automatic refactor requirements.

Exclude or classify generated code, declarative tables, migrations, protocol definitions, and test data separately. A cohesive long parser or schema may be safer than several cyclic fragments. A short module that mixes policy with I/O may already need separation.

Prioritize combinations of evidence: size plus high churn, complexity, broad unrelated public surface, or dependency cycles. Gate intended dependency direction and cycles more strictly than raw LOC. Use fan-in and fan-out contextually: facades and composition roots are expected hubs.

Read [references/evidence-and-sources.md](references/evidence-and-sources.md) before presenting standards, citations, numeric thresholds, or an opinionated architecture policy.

## Handle imports and public APIs

- Keep `__init__.py` deliberate, lightweight, and low in side effects.
- Use documented re-exports and `__all__` to define a supported facade when appropriate; use leading underscores for implementation modules and names.
- Give each public object one canonical documented import path.
- Have internal modules import from the defining module rather than back through the package facade when that avoids cycles and hidden initialization.
- Keep `__main__.py`, CLI adapters, web entry points, and composition roots thin. Let outer layers wire dependencies.
- Isolate optional or heavy dependencies behind backend or adapter modules.
- Treat a circular import as architectural evidence. Prefer merging inseparable modules, extracting a lower-level type or protocol, adding a coordinating module, or inverting a dependency. Use local imports or `TYPE_CHECKING` as tactical mechanisms, not as proof that the architecture is healthy.

When splitting a public module, preserve supported paths with explicit re-exports unless the user authorizes a breaking change. Document deprecation or migration paths when compatibility cannot be preserved.

## Produce a review

Lead with the overall judgment. Then provide:

1. A compact current package map and the observed dependency direction.
2. Prioritized findings, each with concrete file or symbol evidence.
3. For each finding: impact, proposed boundary, compatibility risk, and validation needed.
4. Modules that are long or unusual but should remain as-is, with the reason.
5. A phased refactor plan separating low-risk moves from architectural changes.
6. Relevant source links when invoking external guidance.

Distinguish observations from inferences. Do not report a large file, high fan-in, or an import cycle as self-evidently wrong. Explain the maintenance or correctness consequence in this repository.

## Execute a refactor

1. Characterize existing behavior, public imports, serialization identities, plugin registration, and import-time effects.
2. Add or identify focused tests that protect the behavior and import paths being moved.
3. Select the smallest seam that improves cohesion or dependency direction.
4. Move code with minimal semantic edits; do not combine organization changes with unrelated cleanup.
5. Update internal imports toward defining modules and preserve supported external paths through explicit facades.
6. Remove cycles by changing ownership or dependency direction rather than merely hiding imports.
7. Update documentation, type exports, package data configuration, entry points, and tests affected by physical moves.
8. Inspect the final diff for accidental API expansion, import-time work, duplicated definitions, and unrelated formatting churn.

Prefer incremental, reversible steps over a repository-wide idealized rewrite. Do not add abstractions that merely rename calls; require a clear dependency, testing, stability, or navigation benefit.

## Verify the result

Run the narrowest relevant checks first, then broader configured checks when feasible:

- Targeted tests for moved behavior and public imports.
- Full tests, lint, formatting, and type checking configured by the repository.
- Import smoke tests from an installed build when packaging paths changed.
- Wheel and source-distribution inspection when moving package data or adopting `src/`.
- CLI, plugin, lazy-import, serialization, and documentation examples affected by module paths.
- The inventory script again to confirm intended cycles or dependencies actually changed.

Compare against the baseline and report every check run, any check not run, pre-existing failures, remaining compatibility risk, and intentionally deferred work.
