# Research Engineering Portfolio

[![tests](https://github.com/NEXUSCogOS/research-engineering-portfolio/actions/workflows/tests.yml/badge.svg)](https://github.com/NEXUSCogOS/research-engineering-portfolio/actions/workflows/tests.yml)

I am an independent AI systems and research engineer working on reliable evaluation, evidence quality, provenance and controlled experimentation.

## What this portfolio demonstrates

- designing bounded and testable research questions;
- building small Python evaluation tools and schemas;
- separating observations from claims and authority;
- recording failures, limitations and inconclusive outcomes;
- documenting systems so that another engineer can inspect the reasoning;
- using tests, version control and reproducible reporting practices.

## Selected work

### Evidence-aware evaluation

Designed prototype methods for evaluating whether a successful-looking AI output is supported by valid evidence and remains within its permitted operating boundary.

### Controlled experimental practice

Prepared bounded evaluation studies using predefined questions, conditions, endpoints and claim limits. Work remains experimental and is not presented as independent validation or production qualification.

### Engineering assurance

Built internal tools and documentation for provenance tracking, failure analysis, reproducibility and review of AI-assisted engineering workflows.

## Public engineering samples

The `samples/` directory contains small, generic reference implementations created for this portfolio:

- **Integrity manifests** — create and verify SHA-256 manifests for a directory;
- **Data-quality profiling** — summarize missing and duplicate values in tabular records;
- **Dependency ordering** — produce a deterministic topological order and reject cyclic graphs.

They use only the Python standard library and include automated tests. They demonstrate general engineering practice without exposing private architectures, datasets or research protocols.

Run the checks with:

```bash
python -m unittest discover -s tests -v
```

## Evidence boundary

This public repository is intentionally a high-level portfolio. Its code consists only of generic reference samples. It contains no private source code, system architecture, datasets, prompts, credentials, operational configuration, detailed experimental protocols, commercial plans or protected intellectual property.

The work described here should be read as evidence of research-engineering practice. It does not claim product readiness, commercial traction, independently replicated performance or superiority over other systems.

## Current focus

My current focus is converting experimental engineering work into concise, reproducible research questions and defensible evaluations that can be independently reviewed.

