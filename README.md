# ICFAI College Workflow Investigation and AI/ML Curriculum Redesign

**Institution:** ICFAI Tech, Hyderabad  
**Programme:** B.Tech Artificial Intelligence and Machine Learning  
**Admission Batch:** 2023–2027  
**Submission Date:** 24 October 2026

---

## Project Overview

This repository contains two academic assignments:

1. **Task 1:** Investigation and redesign of a college workflow.
2. **Task 2:** Audit and proposed redesign of the B.Tech Artificial Intelligence and Machine Learning curriculum.

The project includes workflow diagrams, synthetic tests, curriculum analysis, industry comparisons, Python verification scripts, and an interactive Streamlit dashboard.

### Project Objectives

- Analyze a college workflow and identify potential improvements.
- Design a structured workflow with defined responsibilities and approval boundaries.
- Evaluate the proposed workflow using synthetic test cases.
- Review the existing AI/ML curriculum against industry requirements.
- Recommend curriculum improvements while considering academic regulations.
- Evaluate AI-assisted learning exercises using reference tests.
- Present findings through an interactive dashboard.

---

## Task 1 — College Workflow Investigation

**Selected Process:** College Laboratory Booking and Approval System

The selected workflow is a hypothetical process model developed for academic analysis.

It is not presented as an observed, officially implemented, or institutionally approved ICFAI workflow.

### Included Components

- Current workflow diagram
- Proposed workflow diagram
- Evidence log distinguishing assumptions and estimates
- Defined workflow states and approval boundaries
- Five synthetic test cases
- Python workflow verification script
- Estimated time savings and ROI
- Risks, exceptions, and limitations

### Synthetic Test Scenarios

| Test Case | Scenario | Expected Behaviour |
|---|---|---|
| TC01 | Normal booking request | Request follows the approval process |
| TC02 | Missing information | Request requires additional information |
| TC03 | Duplicate booking | Duplicate request is identified |
| TC04 | Unauthorized approval | Unauthorized action is rejected |
| TC05 | Failed processing step | Recovery or fallback procedure is triggered |

The workflow reference script passed five synthetic checks.

These results validate selected model behaviours only and do not establish production readiness.

### Estimated Time Savings

The proposed workflow was evaluated using hypothetical operating assumptions.

| Metric | Estimated Value |
|---|---:|
| Manual processing time | 25 minutes/request |
| Proposed processing time | 8 minutes/request |
| Monthly request volume | 100 |
| Net time saved | 28.25 hours/month |
| Implementation effort | 60 hours |
| Estimated payback period | 2.12 months |

The net savings estimate accounts for assumed review and support effort.

These values are estimates rather than measured institutional outcomes.

### Task 1 Documentation

[View Task 1 Files](Task-1-College-Workflow)

---

## Task 2 — Curriculum Audit and Redesign

**Programme:** B.Tech Artificial Intelligence and Machine Learning  
**Admission Batch:** 2023–2027

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
- Supporting evidence and limitations

### Curriculum Credit Limitation

The current transcription records **135 numeric credits across Semesters I–VI**.

Semesters VII–VIII include grouped or alternative activities whose individual credits have not been allocated in the CSV.

The handbook's displayed semester totals, visible course credits, and printed programme total require reconciliation.

Consequently, the proposed redesign is provisional and is not claimed to be a verified credit-balanced replacement for the complete programme.

### Proposed Curriculum Improvements

The redesign aims to strengthen the following areas:

| Area | Proposed Improvement |
|---|---|
| Programming | More practical coding and testing |
| Machine Learning | Stronger model evaluation practices |
| Deep Learning | Additional implementation exercises |
| Data Engineering | Data processing and pipeline skills |
| MLOps | Model deployment and monitoring concepts |
| Responsible AI | Ethics, fairness, and transparency |
| Software Engineering | Version control and testing practices |

The proposals require institutional and regulatory review before adoption.

### Industry Comparison

Three dated Amazon job descriptions are discussed in:

[Industry Job Comparison](Task-2-Curriculum-Redesign/job_comparison.md)

The analysis considers industry expectations relating to programming, machine learning, software engineering, and practical AI development.

Not all referenced positions are necessarily entry-level graduate roles.

The job descriptions, publication dates, and availability of their original sources require independent verification.

---

## AI-Assisted Exercise Verification

Five AI-assisted exercises were documented across different subjects.

### Verification Results

| Subject | Verification Method | Result |
|---|---|---|
| Computer Programming | Four Python test cases | PASS — 4/4 |
| Data Structures | Four stack-operation tests | PASS — 4/4 |
| Database Management Systems | Three SQLite checks | PASS — 3/3 |
| Machine Learning | Three structural completeness checks | PASS — 3/3 |
| Deep Learning | Three mathematical checks | PASS — 3/3 |
| **Total** | **17 checks** | **17/17 PASS** |

### Verification Scope

The exercises cover:

1. Finding the maximum value in a list without using `max()`.
2. Implementing a stack using Python.
3. Counting approved laboratory bookings using SQL.
4. Explaining data leakage in machine learning.
5. Calculating convolutional layer output dimensions.

The combined verification script completed **17/17 checks successfully**.

However, the Machine Learning checks only verify that the explanation contains a definition, example, and prevention method. They do not independently establish factual correctness.

The results are based on limited reference examples and synthetic test data.

### Verification Files

- [AI Output Verification Report](Task-2-Curriculum-Redesign/ai_output_verification.md)
- [Combined Verification Script](Task-2-Curriculum-Redesign/verify_all_ai_outputs.py)
- [Programming Verification](Task-2-Curriculum-Redesign/verify_programming.py)
- [Data Structures Verification](Task-2-Curriculum-Redesign/verify_data_structures.py)

The provenance and independent validation of the recorded AI-generated responses should be reviewed before treating them as fully verified academic evidence.

### Task 2 Documentation

[View Task 2 Files](Task-2-Curriculum-Redesign)

---

## Interactive Streamlit Dashboard

The project includes an interactive dashboard developed using Python and Streamlit.

### Dashboard Features

- Project overview
- Official curriculum transcription
- Proposed curriculum changes
- Synthetic workflow test cases
- Evidence limitations

### Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Run the Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Testing and Verification

### Task 1 — Workflow Tests

```bash
python Task-1-College-Workflow/test_workflow.py
```

**Previously recorded result:** 5/5 synthetic checks passed.

### Task 2 — Reference Exercise Tests

```bash
python Task-2-Curriculum-Redesign/test_ai_exercises.py
```

**Previously recorded result:** 5/5 reference checks passed.

### Combined AI Output Verification

```bash
python Task-2-Curriculum-Redesign/verify_all_ai_outputs.py
```

**Previously recorded result:** 17/17 checks passed.

### Individual Verification Scripts

Computer Programming:

```bash
python Task-2-Curriculum-Redesign/verify_programming.py
```

Data Structures:

```bash
python Task-2-Curriculum-Redesign/verify_data_structures.py
```

---

## Evidence and Academic Integrity

This project distinguishes between four types of information:

| Evidence Type | Description |
|---|---|
| Observed facts | Information directly supported by identified sources |
| Estimates | Calculations based on stated assumptions |
| Assumptions | Hypothetical workflow rules, request volumes, and timings |
| Proposals | Suggested improvements requiring further validation |

### Academic Integrity Statement

- No confidential student information is included.
- No unauthorized institutional access is claimed.
- No institutional field observation or approval is claimed.
- Synthetic data is used for workflow testing.
- AI assistance was used for drafting, coding, and example generation.
- Known evidence gaps and limitations are documented.
- Verification results are not presented as proof of production readiness.

Supporting evidence is available in the `evidence/` directory.

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

This repository represents an academic prototype and proposal rather than an institutional deployment.

### Outstanding Validation

1. Confirming the applicable official curriculum regulations and credit allocations.
2. Obtaining authorized workflow observations if permission becomes available.
3. Reviewing the provenance and independent verification of recorded AI-generated responses.
4. Obtaining faculty or graduate feedback where feasible.
5. Independently verifying linked industry job descriptions and their dates.
6. Reconciling proposed curriculum changes with full programme credit requirements.

The workflow time savings are hypothetical estimates.

The curriculum redesign requires further academic and regulatory review before implementation.

---

## Final Submission

**Repository:**  
https://github.com/SHIRDIK936/icfai-workflow-curriculum-audit

**Release Tag:** `v1.0.1`

**Release URL:**  
https://github.com/SHIRDIK936/icfai-workflow-curriculum-audit/releases/tag/v1.0.1

**AI Verification Evidence Commit:**  
https://github.com/SHIRDIK936/icfai-workflow-curriculum-audit/commit/db31a4b

**Release Snapshot Commit:** `ad15bcb`

Release `v1.0.1` was tagged from the submission snapshot containing the updated README and AI verification files.

The release tag was pushed to GitHub. Publication of the corresponding GitHub Release should be confirmed separately.

---

## Conclusion

This project presents a hypothetical college workflow redesign and a provisional AI/ML curriculum improvement proposal.

**Task 1** demonstrates process mapping, exception handling, synthetic testing, and estimated operational time savings.

**Task 2** explores curriculum modernization, industry skill alignment, and AI-assisted learning verification.

Together, these assignments demonstrate the application of process analysis, programming, testing, and curriculum evaluation while documenting evidence limitations and areas requiring further validation.
