# ICFAI College Workflow Investigation and AI/ML Curriculum Redesign

**Institution:** ICFAI Tech, Hyderabad  
**Programme:** B.Tech Artificial Intelligence and Machine Learning  
**Admission Batch:** 2023–2027  
**Submission Date:** 24 October 2026

---

## Project Overview

This repository contains two academic assignments:

1. Investigation and redesign of a college workflow.
2. Audit and proposed redesign of the B.Tech Artificial Intelligence and Machine Learning curriculum.

The project includes workflow diagrams, synthetic tests, curriculum analysis, industry comparisons, Python verification scripts, and an interactive Streamlit dashboard.

---

## Task 1 — College Workflow Investigation

**Selected Process:** College Laboratory Booking and Approval System.

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

| Metric | Value |
|---|---|
| Manual processing time | 25 minutes/request |
| Proposed processing time | 8 minutes/request |
| Monthly request volume | 100 |
| Estimated net time saved | 28.25 hours/month |
| Estimated implementation effort | 60 hours |
| Estimated payback period | 2.12 months |

These values are estimates, not measured institutional outcomes.

**Task 1 files:** [Task-1-College-Workflow](Task-1-College-Workflow)

---

## Task 2 — Curriculum Audit and Redesign

**Curriculum Source:** ICFAI Tech Student Handbook 2023–24, Section 4.7.3, page 27.

### Included Components

- Semester-wise curriculum transcription
- KEEP, UPDATE, REDUCE, and ADD recommendations
- Provisional credit-neutral redesign
- Comparison with three dated industry job descriptions
- Five AI-assisted exercise specifications
- Executable reference-solution tests
- AI-output verification report
- Proposed database laboratory
- Evidence and limitations

### Curriculum Credit Limitation

The transcription records 135 numeric credits across Semesters I–VI.

Semesters VII–VIII include grouped or alternative activities whose individual credits have not been allocated in the CSV.

The handbook's displayed semester totals, visible course credits, and printed programme total require reconciliation.

Therefore, the redesign is provisional and is not claimed to be a verified credit-balanced replacement for the complete programme.

### Proposed Curriculum Changes

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

The job postings and their dates require independent verification.

### AI Exercise Verification

Five AI-assisted exercises were documented and evaluated.

| Subject | Verification | Result |
|---|---|---|
| Computer Programming | Four Python test cases | PASS — 4/4 |
| Data Structures | Four stack operation tests | PASS — 4/4 |
| Database Management Systems | Three SQLite checks | PASS — 3/3 |
| Machine Learning | Three structural completeness checks | PASS — 3/3 |
| Deep Learning | Three mathematical checks | PASS — 3/3 |
| **Total** | **17 checks** | **17/17 PASS** |

**Important:** The Machine Learning checks confirm that the explanation includes a definition, example, and prevention method. They do not independently establish factual correctness.

All verification exercises use synthetic examples and limited test coverage.

The AI-generated reference outputs and verification procedures are documented in the project files. Their provenance and independent validation should be reviewed before treating them as fully verified academic evidence.

**Verification files:**

- [AI Output Verification Report](Task-2-Curriculum-Redesign/ai_output_verification.md)
- [Combined Verification Script](Task-2-Curriculum-Redesign/verify_all_ai_outputs.py)
- [Programming Verification](Task-2-Curriculum-Redesign/verify_programming.py)
- [Data Structures Verification](Task-2-Curriculum-Redesign/verify_data_structures.py)

**Task 2 files:** [Task-2-Curriculum-Redesign](Task-2-Curriculum-Redesign)

---

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

---

## Run Tests

### Task 1 — Workflow Tests

```bash
python Task-1-College-Workflow/test_workflow.py
```

### Task 2 — Reference Exercise Tests

```bash
python Task-2-Curriculum-Redesign/test_ai_exercises.py
```

### AI Output Verification

```bash
python Task-2-Curriculum-Redesign/verify_all_ai_outputs.py
```

**Recorded result:** 17/17 checks passed.

---

## Evidence and Academic Integrity

This project distinguishes between:

- **Observed facts:** Information directly supported by identified sources.
- **Estimates:** Quantities calculated using stated assumptions.
- **Assumptions:** Hypothetical workflow rules, request volumes, and process timings.
- **Proposals:** Suggested process and curriculum changes requiring validation.

No confidential student information is used.

No institutional field observation, faculty approval, or employer endorsement is claimed.

AI assistance was used for drafting, coding support, and example generation.

AI-generated outputs require verification, and known limitations are documented.

---

## Repository Structure

```text
icfai-workflow-curriculum-audit/
│
├── README.md
├── requirements.txt
│
├── Task-1-College-Workflow/
│   ├── report.md
│   ├── evidence_log.csv
│   ├── current_workflow.md
│   ├── proposed_workflow.md
│   ├── test_cases.csv
│   ├── test_workflow.py
│   ├── roi_calculation.md
│   └── risks_and_limitations.md
│
├── Task-2-Curriculum-Redesign/
│   ├── report.md
│   ├── official_curriculum.csv
│   ├── proposed_curriculum.csv
│   ├── curriculum_analysis.md
│   ├── job_comparison.md
│   ├── ai_exercises.md
│   ├── test_ai_exercises.py
│   ├── ai_output_verification.md
│   ├── verify_all_ai_outputs.py
│   ├── verify_programming.py
│   ├── verify_data_structures.py
│   ├── lab_design.md
│   └── references.md
│
├── dashboard/
│   └── app.py
│
└── evidence/
    ├── sources.md
    ├── ai_usage_log.md
    └── limitations.md
```

---

## Status and Limitations

This repository is an academic prototype and proposal, not an institutional deployment.

Outstanding validation includes:

1. Confirming the applicable official curriculum regulations and credit allocations.
2. Obtaining authorized workflow observations if permission becomes available.
3. Reviewing the provenance and independent verification of recorded AI-generated responses.
4. Obtaining faculty or graduate feedback where feasible.
5. Independently verifying all linked job postings and preserving their dates.
6. Reconciling the proposed curriculum changes with the full programme credit requirements.

The workflow time savings are hypothetical estimates, and the proposed curriculum changes require institutional review before adoption.

---

## Final Submission

**Repository:**  
https://github.com/SHIRDIK936/icfai-workflow-curriculum-audit

**Planned final release tag:** `v1.0.1`

**Planned final release:**  
https://github.com/SHIRDIK936/icfai-workflow-curriculum-audit/releases/tag/v1.0.1

**AI verification evidence commit:**  
https://github.com/SHIRDIK936/icfai-workflow-curriculum-audit/commit/db31a4b

The evidence commit contains the additional AI-output verification files.

The final release tag will identify the complete submission snapshot after publication.

---

## Conclusion

This project presents a hypothetical college workflow redesign and a provisional AI/ML curriculum improvement proposal.

The workflow component demonstrates process mapping, exception handling, synthetic testing, and estimated time savings.

The curriculum component explores course modernization, industry skill alignment, and AI-assisted learning verification.

Together, these assignments demonstrate the application of process analysis, programming, testing, and curriculum evaluation while documenting evidence limitations and areas requiring further validation.