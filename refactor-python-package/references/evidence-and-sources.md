# Evidence and sources for Python package organization

Use this reference to support recommendations without presenting local preferences as Python rules. The source set contains official language and packaging guidance, maintainer documentation, well-regarded practitioner guidance, and research about metric thresholds and change evidence. It contains **no empirical evidence for an optimal Python module length**.

## Evidence labels

- **Official guidance**: Python, PyPA, Django, or another project's normative documentation.
- **Maintainer guidance**: documentation for a tool or library, describing supported behavior or conventions.
- **Practitioner guidance**: reasoned design advice from experienced maintainers or authors; useful, but not normative.
- **Empirical evidence**: measurements or controlled studies. Use it within the studied population and limitations; none of the sources below establishes a universal Python module-size threshold.
- **Local heuristic**: a review prompt or policy adopted for this skill. State it as a heuristic, never as a community standard.

## Principles to apply

### Prefer cohesion and dependency direction over file length

- Organize a module around one nameable concept, responsibility, or invariant.
- Keep definitions together when they use the same vocabulary, change together, and share private helpers.
- Split when independently nameable regions change for different reasons, serve different callers, or depend on different subsystems.
- Separate pure domain logic from CLI, framework, filesystem, network, database, and serialization concerns when that creates a simpler dependency direction.
- Prefer a small, stable interface over many shallow pass-through modules.
- Avoid both "spaghetti" (entangled responsibilities) and "ravioli" (excessively tiny, weak modules).

The official Django design philosophy explicitly values loose coupling and tight cohesion. Cosmic Python develops the same idea through dependency inversion, abstractions, and architectural boundaries.

### Treat module length as a signal, not a rule

Python and PEP 8 define no maximum module length. Pylint exposes `max-module-lines`, with a documented default of 1,000 lines, but its `too-many-lines` message is a convention check—not evidence that 1,001 lines is a design defect.

Use these **local heuristics** when the project has no existing policy:

- Around 500–600 hand-written lines: pause and review cohesion, dependency shape, and change patterns.
- At 1,000 lines: consider a warning or require an intentional justification.
- Do not split solely to satisfy a count.
- Exempt or separately assess generated files, migrations, large declarative tables, and data-heavy tests.

The relevant question is whether the file hides multiple responsibilities or unstable boundaries. A cohesive 900-line parser can be healthier than nine mutually dependent 100-line files; a 150-line file mixing CLI wiring, database access, and domain rules may already need separation.

### Design imports as architecture

- Aim for one-way dependencies, such as `cli/backends -> parsing/analysis -> model`.
- Keep the core independent of interfaces, storage, and frameworks.
- Treat repeated circular imports as architectural evidence: modules may belong together, or both may depend on a missing lower-level abstraction.
- Use local imports or `TYPE_CHECKING` only when they solve an intentional runtime or typing constraint; do not let them conceal a confused dependency graph.
- Consider enforcing intended layers, forbidden imports, sibling independence, or acyclicity in CI with Import Linter.

The Python FAQ explains the mechanics and limitations of mutually importing modules. It does not prescribe a complete architecture; use dependency-inversion guidance to decide whether to merge, extract, or invert.

### Make the public API deliberate

- Keep `__init__.py` lightweight and use it as a deliberate facade only when that benefits callers.
- Mark internal modules and names with a leading underscore.
- Use `__all__` to document intended exports where appropriate.
- Give each public object one canonical import path.
- Inside the package, prefer importing from the defining module instead of routing every internal import through the package facade.
- Treat published module paths and re-exports as compatibility commitments.
- Check import-time and cycle costs before adding eager re-exports.

PEP 8 supplies the official public-versus-internal conventions. Griffe and Scientific Python add practical guidance for API discovery, exports, re-exports, and tooling.

### Choose `src/` layout intentionally

For a distributable package, default to `src/<package>/` when it is useful to ensure tests and development commands import the installed package rather than an accidental working-tree copy. Validate by building and testing the installed artifact.

This is a packaging and test-isolation decision, not a universal requirement. PyPA documents the tradeoffs between `src` and flat layouts; Hynek Schlawack gives a practitioner explanation centered on testing the same artifact users install.

## Review questions

- Can the module be described without joining unrelated concerns with “and”?
- Which definitions enforce the same invariants or usually change together?
- Do distinct regions depend on different libraries or runtime services?
- Can pure logic be tested without configuring infrastructure?
- Do callers consistently use only unrelated subsets of the module?
- Is a cycle revealing misplaced ownership, a missing abstraction, or a module split that should be undone?
- Would the proposed split reduce coupling, or merely add forwarding imports and navigation?
- Are public imports intentional, stable, and documented?
- Does the test setup verify the installed package rather than an in-tree copy?

## Metrics caveats

Line count, number of definitions, cyclomatic complexity, fan-in/fan-out, import cycles, and churn can help locate review targets. None determines the correct boundary by itself.

- Use metrics to rank files for inspection, not to automate structural conclusions.
- Interpret complexity in context: parsers, protocol implementations, generated bindings, and declarative schemas have different shapes.
- Use version-control churn and co-change only as supporting evidence; frequently co-changing code may belong together, while stable but coupled code can still be poorly designed.
- Record the reason for a split in terms of responsibility, dependency, testability, or public API—not just a reduced line count.
- If adopting a numeric policy, label it as project-local and allow documented exceptions.

**Empirical-evidence caveat:** the sources collected here do not include a study showing that a particular number of lines per Python module improves defects, maintainability, or comprehension. Do not describe the 500–600 review point or Pylint's 1,000-line default as empirically validated.

## Annotated sources

### Official guidance

1. [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
   Official Python style guidance. Relevant for naming, imports, and conventions, but it sets no module-length limit.

2. [PEP 8 — Public and Internal Interfaces](https://peps.python.org/pep-0008/#public-and-internal-interfaces)
   Official conventions for public APIs, `__all__`, and leading underscores. Use this to distinguish compatibility commitments from internal implementation.

3. [Python FAQ — mutually importing modules](https://docs.python.org/3/faq/programming.html#how-can-i-have-modules-that-mutually-import-each-other)
   Official explanation of circular-import behavior and import placement. Useful for mechanics; it is not an architectural endorsement of cycles.

4. [PyPA — `src` layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
   Official packaging discussion of the tradeoffs, including import isolation, editable installs, and convenience. Prefer this for current layout guidance.

5. [Django design philosophies](https://docs.djangoproject.com/en/6.0/misc/design-philosophies/)
   Official Django project principles, including loose coupling and tight cohesion. Broad design guidance rather than a package template.

6. [Python tutorial — Modules and Packages](https://docs.python.org/3/tutorial/modules.html)
   Official explanation of modules, packages, `__init__.py`, `__all__`, and intra-package imports. It explains mechanics and namespaces without prescribing file size or one-class-per-file organization.

7. [pytest — Good Integration Practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
   Official pytest guidance on test placement, installed-package testing, import modes, and `src/` layouts. Use when a physical move can change which copy of a package tests import.

### Maintainer and tool guidance

8. [Pylint configuration — `max-module-lines`](https://pylint.readthedocs.io/en/stable/user_guide/configuration/all-options.html#max-module-lines)
   Documents the configuration and its 1,000-line default. This is a tool convention, not a Python standard or empirical threshold.

9. [Pylint — `too-many-lines`](https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/too-many-lines.html)
   Explains the warning and why long modules may merit review. Use as a prompt to inspect design, not as proof that a split is required.

10. [Griffe — Design your public API](https://mkdocstrings.github.io/griffe/guide/users/recommendations/public-apis/)
   Maintainer guidance on public names, aliases, exports, and API-documentation behavior. Especially useful for typed or documented libraries.

11. [Scientific Python — Exports](https://learn.scientific-python.org/development/patterns/exports/)
   Maintainer-community guidance on `__all__`, re-exports, import costs, and stable user-facing namespaces.

12. [Import Linter — contract types](https://import-linter.readthedocs.io/en/stable/contract_types/)
    Tool documentation for enforcing layers, forbidden dependencies, independent siblings, and acyclic graphs.

### Practitioner guidance

13. [The Hitchhiker's Guide to Python — Structuring Your Project](https://docs.python-guide.org/writing/structure/)
    A useful overview of repository structure, coupling, circular dependencies, global state, spaghetti, and ravioli code. Its architectural vocabulary remains helpful, but its repository-layout and packaging advice is dated; prefer current PyPA guidance for `src` layout and packaging decisions.

14. [Cosmic Python — Inversion of Control](https://www.cosmicpython.com/blog/2019-04-15-inversion-of-control)
    Explains architectural responses to dependency and import problems, including inversion of control. Useful when a cycle is a symptom rather than merely an import-order issue.

15. [Cosmic Python — Coupling and Abstractions](https://www.cosmicpython.com/book/chapter_03_abstractions.html)
    A worked explanation of selecting abstractions and boundaries to reduce coupling and improve testability.

16. [Architecture Patterns with Python — Introduction](https://www.cosmicpython.com/book/introduction.html)
    Introduces domain, service, adapter, entrypoint, and composition-root boundaries through a complete architectural approach. Apply selectively; small packages rarely need every layer.

17. [Hynek Schlawack — Testing & Packaging](https://hynek.me/articles/testing-packaging/)
   Practitioner rationale for `src` layout and testing installed distributions, focused on avoiding false confidence from working-tree imports.

18. [John Ousterhout — Modular Design](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign)
   A language-independent argument for “deep modules”: substantial functionality behind a small interface. Use as a counterweight to mechanical file-splitting, not as a Python-specific size rule.

### Case studies and empirical evidence

19. [NumPy NEP 52 — Python API cleanup for NumPy 2.0](https://numpy.org/neps/nep-0052-python-api-cleanup.html)
   A real package-maintainer case study in reducing accidental exports, aliases, and ambiguous namespaces while establishing canonical public locations.

20. [Alves, Ypma, and Visser — Deriving Metric Thresholds from Benchmark Data](https://webarchive.di.uminho.pt/wiki.di.uminho.pt/twiki/pub/Personal/Joost/PublicationList/AlvesYpmaVisserICSM2010.pdf)
   Shows why metric thresholds should be calibrated from representative benchmark distributions rather than assumed universal. It is not Python-specific and does not establish a module-length target.

21. [Nagappan and Ball — Use of Relative Code Churn Measures to Predict System Defect Density](https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/)
   Supports using normalized change history as one signal for review prioritization. It studies one large Windows system, so do not generalize its predictive results into a universal refactoring rule.

## Citation discipline

When producing a review or refactor plan:

- Cite official guidance for factual claims about Python conventions and packaging behavior.
- Cite maintainer documentation for tool behavior and configuration.
- Present Cosmic Python, Hynek, the Hitchhiker guide, Ousterhout, Griffe, and Scientific Python as informed design guidance, not binding standards.
- State the population and limitation when using empirical work; do not convert cross-language correlations into Python design mandates.
- State explicitly that numeric file-size thresholds are local heuristics unless the project already defines its own policy.
- Do not claim empirical support that is absent from this source set.
