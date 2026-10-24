# ICFAI College Workflow Investigation and AI/ML Curriculum Redesign

**Institution:** ICFAI Tech, Hyderabad  
**Programme:** B.Tech Artificial Intelligence and Machine Learning  
**Admission Batch:** 2023–2027  
**Submission Date:** 24 October 2026

## Project Overview

This repository contains two academic assignments:

1. Investigation and redesign of a college workflow.
2. Audit and proposed redesign of the B.Tech Artificial Intelligence and Machine Learning curriculum.

The project includes workflow diagrams, synthetic tests, curriculum analysis, industry comparisons, Python verification scripts, and an interactive Streamlit dashboard.

## Task 1 — College Workflow Investigation

**Selected process:** College Laboratory Booking and Approval System.

This is a hypothetical process model prepared for academic analysis. It is not presented as an observed or institutionally approved ICFAI workflow.

### Included Components

- Current workflow diagram
- Proposed workflow diagram
- Evidence log with assumptions and estimates
- Defined workflow states and approval boundaries
- Five synthetic test cases
- Python workflow test script
- Estimated time savings and ROI
- Risks and limitations

### Synthetic Test Scenarios

1. Normal booking request
2. Missing information
3. Duplicate booking
4. Unauthorized approval
5. Failed processing step

The reference workflow script passed five synthetic checks. These tests do not establish production readiness.

### Estimated Time Savings

Under the stated hypothetical assumptions:

- Manual processing: 25 minutes per request
- Proposed processing: 8 minutes per request
- Request volume: 100 per month
- Estimated net time saved: 28.25 hours per month
- Estimated implementation effort: 60 hours
- Estimated payback: approximately 2.12 months

These values are estimates, not measured outcomes.

**Task 1 files:** [Task-1-College-Workflow](Task-1-College-Workflow)

## Task 2 — Curriculum Audit and Redesign

**Curriculum source:** ICFAI Tech Student Handbook 2023–24, Section 4.7.3, page 27.

### Included Components

- Semester-wise curriculum transcription
- KEEP, UPDATE, REDUCE, and ADD recommendations
- Provisional credit-neutral redesign
- Comparison with three dated industry job descriptions
- Five AI-assisted exercise specifications
- Executable reference-solution tests
- Proposed database laboratory
- Evidence and limitations

### Curriculum Credit Limitation

The transcription records 135 numeric credits across Semesters I–VI.

Semesters VII–VIII include grouped or alternative activities whose individual credits have not been allocated in the CSV.

The handbook's displayed semester totals, visible course credits, and printed programme total require reconciliation. Therefore, the redesign is provisional and is not claimed to be a verified credit-balanced replacement for the complete programme.

### Proposed Changes

The proposed redesign retains core programming and mathematical foundations while strengthening:

- Machine learning evaluation
- Deep learning practice
- Data engineering
- Model deployment and MLOps
- Responsible AI
- Practical software testing

### Industry Comparison

Three dated Amazon job descriptions are documented in `job_comparison.md`.

The comparison identifies skills relevant to applied AI roles but does not imply that every posting is an entry-level graduate role.

### AI Exercise Verification

Reference exercises cover:

1. Computer Programming
2. Data Structures
3. Database Management Systems
4. Machine Learning
5. Deep Learning

The Python reference tests passed 5/5 checks.

These checks verify prepared reference solutions, not actual responses from an AI assistant.

**Task 2 files:** [Task-2-Curriculum-Redesign](Task-2-Curriculum-Redesign)

## Interactive Dashboard

The Streamlit dashboard displays:

- Project overview
- Official curriculum transcription
- Proposed curriculum changes
- Synthetic workflow test cases
- Evidence limitations

### Installation

```bash
pip install -r requirements.txt
```

### Run Dashboard

```bash
streamlit run dashboard/app.py
```

## Run Tests

### Task 1

```bash
python Task-1-College-Workflow/test_workflow.py
```

### Task 2

```bash
python Task-2-Curriculum-Redesign/test_ai_exercises.py
```

## Evidence and Academic Integrity

This project distinguishes:

- **Observed facts:** Information directly supported by identified sources.
- **Estimates:** Quantities calculated using stated assumptions.
- **Assumptions:** Hypothetical workflow rules, request volumes, and process timings.
- **Proposals:** Suggested process and curriculum changes requiring validation.

No confidential student information is used.

No institutional field observation, faculty approval, or employer endorsement is claimed.

AI assistance was used for drafting and coding support. Outputs require independent verification, and limitations are documented.

## Repository Structure

```text
icfai-workflow-curriculum-audit/
├── README.md
├── requirements.txt
├── Task-1-College-Workflow/
│   ├── report.md
│   ├── evidence_log.csv
│   ├── current_workflow.md
│   ├── proposed_workflow.md
│   ├── test_cases.csv
│   ├── test_workflow.py
│   ├── roi_calculation.md
│   └── risks_and_limitations.md
├── Task-2-Curriculum-Redesign/
│   ├── report.md
│   ├── official_curriculum.csv
│   ├── proposed_curriculum.csv
│   ├── curriculum_analysis.md
│   ├── job_comparison.md
│   ├── ai_exercises.md
│   ├── test_ai_exercises.py
│   ├── lab_design.md
│   └── references.md
├── dashboard/
│   └── app.py
└── evidence/
    ├── sources.md
    ├── ai_usage_log.md
    └── limitations.md
```

## Status and Limitations

This repository is an academic prototype and proposal, not an institutional deployment.

Outstanding validation includes:

- Confirming the applicable official curriculum regulations and credit allocations.
- Obtaining authorized workflow observations if permission becomes available.
- Running and recording actual AI-generated exercise responses.
- Obtaining faculty or graduate feedback where feasible.
- Independently verifying all linked job postings and preserving their dates.

## Release

The final submission release is linked here after publication.

**Release tag:** `v1.0.0`