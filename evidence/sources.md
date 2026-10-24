# Evidence Sources

**Prepared:** 24 October 2026

## Task 1 — Workflow Investigation

The College Lab Booking and Approval System is a hypothetical case study.

- **Observed institutional facts:** None collected through field observation.
- **Assumptions:** Booking stages, staff responsibilities, authorization rules, exception handling, and request volume.
- **Estimates:** Processing times, support effort, rework reduction, and implementation effort.
- **Synthetic evidence:** Five workflow test scenarios and their executable checks.

The dated evidence log is available in `../Task-1-College-Workflow/evidence_log.csv`.

No real institutional booking records or confidential information were used.

## Task 2 — Curriculum Audit

**Primary curriculum source:** ICFAI Tech Student Handbook 2023–24, Section 4.7.3, page 27, B.Tech Artificial Intelligence and Machine Learning.

The handbook page was supplied for the assignment. Course names and credits were transcribed into `official_curriculum.csv`.

**Limitation:** The applicable regulations, programme credit total, and final-year allocations have not been fully reconciled.

## Industry Sources

Three Amazon job descriptions were used for comparison:

1. Applied Scientist II, Amazon Music — Job ID 10542475, posted 22 October 2026.
2. Senior Applied Scientist, Buyer Risk Prevention — Job ID 10531907, reported posted 22 October 2026.
3. Applied Scientist I — Job ID 10421937, posted 17 May 2026.

Original job links and the comparison are recorded in `../Task-2-Curriculum-Redesign/job_comparison.md`.

## Verification Evidence

- Task 1: `test_workflow.py` — five synthetic workflow checks.
- Task 2: `test_ai_exercises.py` — five reference-solution checks.
- Dashboard: `dashboard/app.py` — interactive presentation of recorded project data.

Passing synthetic tests does not demonstrate that the proposed systems were deployed or validated in real institutional settings.