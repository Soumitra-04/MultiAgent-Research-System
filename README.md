# Multi-Agent Research System

A modular, agentic research platform designed to investigate claims, gather evidence, validate sources, and generate structured research reports using specialized AI agents.

## Overview

This project aims to build a research pipeline where multiple agents collaborate to:

* Validate user input
* Detect prompt injection attempts
* Classify claims
* Decompose research problems
* Gather evidence from multiple sources
* Track provenance and citations
* Analyze contradictions
* Generate evidence-backed conclusions

The system is designed around a database-backed workflow that allows every claim, task, source, and research session to be traced throughout the entire pipeline.


## Planned Agent Architecture

### Agent 0 — Input Validator

Responsibilities:

* Validate user input
* Detect prompt injection
* Compute risk score
* Gate entry into the pipeline

### Agent 1 — Planner

Responsibilities:

* Understand the claim
* Classify claim type
* Generate research strategy
* Create research tasks

Example classifications:

* Factual
* Causal
* Predictive
* Comparative
* Ethical

### Agent 2 — Research Coordinator

Responsibilities:

* Assign research tasks
* Manage workflow execution
* Track progress

### Agent 3 — Evidence Collector

Responsibilities:

* Gather information from external sources
* Store findings
* Track provenance

### Agent 4 — Evidence Verifier

Responsibilities:

* Verify source quality
* Check credibility
* Flag weak evidence

### Agent 5 — Contradiction Analyzer

Responsibilities:

* Compare competing claims
* Identify conflicts
* Highlight uncertainty

### Agent 6 — Synthesizer

Responsibilities:

* Merge findings
* Build evidence-backed narrative
* Generate conclusions

### Agent 7 — Report Generator

Responsibilities:

* Produce final research report
* Generate citations
* Present confidence levels

---

## Planned Data Sources

### Search

* Tavily
* Serper

### Academic Research

* Semantic Scholar
* Arxiv
* CrossRef
* PubMed

### Community Knowledge

* Reddit (PRAW)

### Encyclopedic Knowledge

* Wikimedia APIs

### Web Extraction

* BeautifulSoup
* Firecrawl
* Playwright

---

## Project Structure

```text
MultiAgent_Research_System/
│
├── agents/
│
├── database/
│   ├── schemas/
│   ├── migrations/
│   └── db_helpers.py
│
├── tools/
│   ├── input_validator.py
│   └── ...
│
├── graphs/
│
├── memory/
│
├── reports/
│
├── tests/
│
├── main.py
│
└── README.md
```

---

## Example Workflow

```text
User Claim
    ↓
Input Validator
    ↓
Planner Agent
    ↓
Task Generation
    ↓
Evidence Collection
    ↓
Evidence Verification
    ↓
Contradiction Analysis
    ↓
Research Synthesis
    ↓
Final Report
```

---

## Technology Stack

* Python
* LangGraph
* LangChain
* SQLite
* Pydantic
* Loguru
* Tavily
* PRAW
* Wikimedia APIs

---

## Long-Term Goals

* Deep research capabilities
* Multi-agent orchestration
* Source provenance tracking
* Evidence graphs
* Knowledge base construction
* Human-in-the-loop verification
* Research report generation
* Autonomous claim investigation

---

## Status

🚧 Active Development

Current milestone:
Core infrastructure completed.

Next milestone:
Planner Agent and claim-classification system.
