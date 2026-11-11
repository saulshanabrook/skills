# Source guidance and a bounded example corpus

This reference distinguishes **advice explicitly given by a guide** from **organizational patterns observed in papers** and the skill's adaptations. The four guides and sixteen paper examples were reread in November 2026. This is a selected corpus, largely e-graph and provenance work with two Rust-verification examples, not a representative study or a universal PL norm. Summaries are paraphrases, not reproduced sections.

Use an example to understand a writing choice, then return to the source if borrowing its technical comparison. Historical claims about priority, capabilities, maintenance, performance, and missing proofs require fresh verification. Physical PDF pages refer to the specified version; they are not interchangeable with published pagination. Some examples intentionally merge related work with background, discussion, or conclusions.

## Four writing guides: prescriptions and adaptations

### Michael Ernst — How to write a technical paper or a research paper

[Guide](https://homes.cs.washington.edu/~mernst/advice/write-technical-paper.html), April 2005, updated July 1, 2024. Relevant headings: “Related work,” “Know your message, and stay on message,” organization, and “Feedback.” HTML; no physical PDF pagination.

**Explicit advice:** explain contributions and connections among approaches rather than listing abstracts; organize around a clear message and reader; outline and use feedback to repair misunderstandings. Ernst generally favors late related work.

**Adaptation:** identify the manuscript's argument before expanding the literature. A reader's confusion is evidence to investigate, not a command to accept every proposed fix. Neither fixed subsection counts nor citation formulas follow.

### Jennifer Widom — Tips for Writing Technical Papers

[Guide](https://cs.stanford.edu/people/widom/paper-writing.html), January 2006, with later presentation/revision notes. Relevant headings: “Related Work,” “The Introduction,” “The Body,” and “Citations.” HTML; no physical PDF pagination.

**Explicit advice:** choose early or late placement according to whether concise immediate positioning or technical prerequisites matter; an early summary may precede detailed later comparison. Present the argument rather than the discovery history; distinguish inherited background; check bibliography completeness and consistency.

**Adaptation:** keep essential attribution where machinery is introduced and place detailed comparison where readers can assess it. The guide's introduction outline is an aid, not a fixed PL paragraph template.

### Simon Peyton Jones — How to Write a Great Research Paper

[Author page](https://simon.peytonjones.org/great-research-paper/); reviewed [52-page deck](https://www.microsoft.com/en-us/research/uploads/prod/2016/07/How-to-write-a-great-research-paper.pdf). Physical PDF pp.12–13: central idea; 21–25: contributions/evidence; 27–30: placement; 31–32: credit; 36–39: examples; 41–44: feedback/criticism. Use this deck's actual page count rather than metadata for another talk.

**Explicit advice:** establish the idea before detailed comparison, state contributions and evidence, credit predecessors, acknowledge limits, avoid disparaging competitors, and obtain feedback. The deck strongly prefers late placement.

**Adaptation:** a predecessor can be a foundation or complement, not only a deficit. Placement advice must be weighed with reader needs and other guides. Advice to seek expert feedback does not authorize contacting people.

### Stefanie Tellex — Writing a Technical Paper

[Guide](https://h2r.cs.brown.edu/writing-a-technical-paper/), October 24, 2019. Relevant headings: “Related Work,” “Abstracts and Introductions,” and “Technical Approach.” HTML; no physical PDF pagination.

**Explicit advice:** develop short paper-specific summaries and comparisons, cluster them, and write group-level synthesis; retain useful notes and give very close work more space. Tellex prefers early placement but permits later technical comparisons.

**Adaptation:** paper-first research notes and relationship-led final prose serve different stages. Do not turn the guide's robotics abstract template or citation-package preference into a universal PL requirement.

**Tensions retained:** these guides differ on placement. They support coherent grouping without one mandatory hierarchy. Their advice supports credit and comparison, not a requirement that every difference imply superiority. Bounded parallel evidence checks are an agent-workflow adaptation, not advice directly prescribed by the guides.

## Sixteen paper examples: observed organization

### 1. egg: Fast and Extensible Equality Saturation

POPL 2021, [DOI](https://doi.org/10.1145/3434304); reviewed [arXiv:2004.03082v3](https://arxiv.org/pdf/2004.03082v3), November 7, 2020. §7 “Related Work,” physical PDF pp.25–26.

**Observed:** four run-in topics cover rewriting, e-graphs/matching, congruence closure, and superoptimization. The nearest algorithm comparison isolates when invariants are restored and the workload, while other paragraphs credit compatible techniques. It opens with history and closes with possible portability, not a stock superiority statement.

### 2. Better Together: Unifying Datalog and Equality Saturation

PLDI 2023, PACMPL 7, Article 125, [DOI](https://doi.org/10.1145/3591239). Reviewed published PDF, §7 “Related Work,” physical PDF pp.20–22, printed 125:20–125:22.

**Observed:** headings name the traditions being combined: e-graphs, databases/Datalog, and logic programming/theorem proving. Paragraphs distinguish inherited mechanisms, changed goals, and open directions. The synthesis drives the grouping; a semantic connection is not presented as an implemented capability.

### 3. Efficient Extraction for Effectful E-graphs

PACMPL 10, OOPSLA2, Article 398, October 2026, [DOI](https://doi.org/10.1145/3839530). Reviewed publication-identifying PDF, §9 “Related Work,” physical PDF p.25, printed 398:25.

**Observed:** the nearest effect-safe predecessor is separated from pure extraction and systems that avoid the problem through restrictions or another task. Its compact organization establishes whether systems solve the same problem before comparing guarantees. Neither its length nor its assertive judgments are universal templates.

### 4. Relational E-matching

PACMPL 6, POPL, Article 35, 2022, [DOI](https://doi.org/10.1145/3498696). Reviewed §6 “Discussion,” physical PDF pp.19–21, printed 35:19–35:21; no dedicated related-work section.

**Observed:** five subsections follow consequences of the relational design: representation, pushdown, joins, incremental processing, and existing database systems. It credits older encodings and separates implemented choices, optimization possibilities, and an SQLite prototype with limitations. Comparisons can be integrated with discussion rather than placed in a standalone catalogue.

### 5. Small Proofs from Congruence Closure

FMCAD 2022; reviewed [arXiv:2209.03398v1](https://arxiv.org/pdf/2209.03398v1). §II “Background and Related Work,” physical PDF pp.2–3, no printed page labels in the reviewed copy.

**Observed:** definitions and a running example precede explanation machinery and the nearest shrinking method. The final comparison isolates cost and dependence on retained alternatives. Merged background makes the technical distinction understandable; it does not imply every section must begin with the new contribution.

### 6. Dis/Equality Graphs

PACMPL 9, POPL, Article 77, January 2025, [DOI](https://doi.org/10.1145/3704913). §7 “Related Work,” physical PDF pp.20–22, printed 77:20–77:22.

**Observed:** ecosystem paragraphs precede topics on extensions, theorem provers/SMT, and formalisms. System capabilities and formal results are compared along distinct axes, including the questions an abstraction can settle. The broader introduction does not establish a requirement to add background padding.

### 7. Parallel and Customizable Equality Saturation

CC 2026, [DOI](https://doi.org/10.1145/3771775.3786266). Reviewed 12-page conference PDF, §8 “Related Work,” physical PDF pp.10–11, printed pp.103–104.

**Observed:** a grouped library comparison is followed by short paragraphs on complementary extraction, matching, and slicing techniques, then compiler integration. One-paper paragraphs work because each establishes a distinct relationship. Prospective combinations are separated from demonstrated results; headings are unnecessary for this compact argument.

### 8. RustBelt: Securing the Foundations of the Rust Programming Language

PACMPL 2, POPL, Article 66, 2018, [DOI](https://doi.org/10.1145/3158154); reviewed [34-page author PDF](https://people.mpi-sws.org/~dreyer/papers/rustbelt/paper.pdf). §8 “Related Work,” physical PDF pp.29–31, printed 66:29–66:31.

**Observed:** unequal space goes to substructural type systems, Rust formal results, and separation logics. The main comparison disambiguates different meanings of extensibility and credits supporting infrastructure. The last paragraph is a qualified future connection, not a final superiority claim.

### 9. Aeneas: Rust Verification by Functional Translation

Published 2022, [DOI](https://doi.org/10.1145/3547647); reviewed 43-page [arXiv:2206.07185v2](https://arxiv.org/pdf/2206.07185v2), September 28, 2022. §8 “Related Work; Conclusion,” physical/printed PDF pp.39–41; comparison Figure 14 is on physical p.32. Publication pagination differs.

**Observed:** starts with the nearest predecessor, then separates complementary goals, foundations, workflows, and shared mechanisms. It acknowledges stronger guarantees in another system. Its final position statement belongs to a merged conclusion; it is not evidence for mandatory paragraph endings.

### 10. Declarative Datalog Debugging for Mere Mortals

Köhler, Ludäscher, Smaragdakis, 2012; reviewed [author PDF](https://www.cs.ucdavis.edu/~ludaesch/pubs/DeclarativeDebugging.pdf), §5 “Related Work,” physical PDF pp.10–11, no printed page labels.

**Observed:** moves from an older debugging family to a closer graph-based debugger, then bridges to database provenance and semirings. Different paragraphs distinguish architecture, compare navigation/profiling, or explain a mathematical connection. The final paragraph develops that connection rather than recapitulating novelty.

### 11. Debugging Large-scale Datalog: A Scalable Provenance Evaluation Strategy

Zhao, Subotić, Scholz, TOPLAS 42(2), Article 7, April 2020; reviewed [published PDF](https://souffle-lang.github.io/pdf/toplas20.pdf), §6 “Related Work,” physical PDF pp.31–32, printed 7:31–7:32.

**Observed:** separates debugging frameworks, provenance production, other applications, other areas, and lattice ingredients. It locates novelty in generation rather than the user-facing framework. Paragraphs establish compatibility and inheritance as well as differences. Its broad historical claims are source statements to verify, not reusable writing formulas.

### 12. Provenance Traces — Extended Report

Cheney, Acar, Ahmed; reviewed [arXiv:0812.0564v1](https://arxiv.org/pdf/0812.0564v1), December 2, 2008. The supplied copy also prints a 2018/10/22 footer. §7 “Related and future work,” physical/printed PDF p.18.

**Observed:** conceptual paragraphs span provenance models, updates, workflows, adaptive computation, bidirectional computation, and analyses. They credit inspiration, acknowledge an unhandled setting, and weave in future work. It explicitly bounds its coverage of dynamic analysis; a paragraph need not assert an advantage.

### 13. Database Queries that Explain their Work

Cheney, Ahmed, Acar, PPDP 2014, [DOI](https://doi.org/10.1145/2643135.2643143). Reviewed repository peer-reviewed version with a cover page, §8 “Related and future work,” physical PDF pp.12–13, printed pp.11–12.

**Observed:** starts with slicing, groups provenance models and workflow formalizations, explains its own prior work, and closes with future directions. Semantic capabilities govern the comparisons. An intellectual chain can be developed in one paragraph; the authors' earlier work is inherited context, not merely another competitor.

### 14. Lineage Capture Trade-offs: A Case Study in DuckDB

Mohammed and Wu, ProvenanceWeek 2025, [DOI](https://doi.org/10.1145/3736229.3736265). Reviewed five-page publication PDF, §4 “Related Work,” physical PDF p.4, printed p.35.

**Observed:** three paragraphs follow the study's query/operator/function-level taxonomy. A one-sentence citation bundle and a longer mechanism comparison coexist. The section supplies context for an empirical study without independently repeating its thesis or results. No fixed paragraph length, citation count, or repeated contribution sentence follows.

### 15. HoTTSQL: Proving Query Rewrites with Univalent SQL Semantics

Chu, Weitz, Cheung, Suciu; reviewed [arXiv:1607.04822v2](https://arxiv.org/pdf/1607.04822v2), August 5, 2016, footer 2016/8/9, rather than inferring a version from a 2017 filename. §6 “Related Work,” §§6.1–6.3, physical/printed PDF pp.11–12.

**Observed:** separates rewrite rules, SQL semantics, and broader proof-system precedents. It credits specific encodings and expressly limits its verification scope. The broader verification catalogue has no final contrast with HoTTSQL. Contribution positioning can coexist with ingredient attribution and methodological context.

### 16. ProvSQL: A General System for Keeping Track of the Provenance and Probability of Data

Sen, Maniu, Senellart; reviewed a supplied copy catalogued as 2025, with no explicit version/date on its examined title page. §II “Related Systems,” physical PDF p.2, no printed page label. [Public work record](https://arxiv.org/abs/2504.12058) is unversioned and may serve later revisions; do not substitute later pagination or claims silently.

**Observed:** named systems organize comparisons of deployment, feature coverage, and scalability; one paragraph groups systems by obsolescence. Fuller comparisons justify evaluation baselines and credit features absent from ProvSQL. System-by-system treatment is useful when each baseline requires a different decision-relevant comparison; maintenance claims need date-sensitive checking.

## How to use the corpus

Choose examples by rhetorical need, not topic keyword alone. For mechanism contrasts, inspect egg or the Datalog debugger. For a synthesis of traditions, inspect egglog. For guarantee and scope distinctions, inspect RustBelt, Aeneas, or HoTTSQL. For compact taxonomy-led comparison, inspect the DuckDB study. For complementary systems or baseline selection, inspect Foresight or ProvSQL.

Across these examples, useful paragraph jobs include explanation, credit, nearest-predecessor comparison, intellectual lineage, compatibility, limitations, and future connections. The corpus supplies counterexamples to mandatory historical openings, one-paper paragraphs, technique-only grouping, repeated present-work endings, fixed heading/count rules, and a universal concluding novelty summary. The skill's workflow is an adaptation for source-grounded manuscript collaboration, not a claim that the papers prescribe it.
