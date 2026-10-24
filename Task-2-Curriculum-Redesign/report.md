# TASK 2: CURRICULUM AUDIT AND REDESIGN

## 1. Introduction

**Institution:** ICFAI Tech, Hyderabad  
**Programme:** B.Tech Artificial Intelligence and Machine Learning  
**Admission Batch:** 2023–2027  
**Review Date:** 24 October 2026  
**Primary Source:** ICFAI Tech Student Handbook 2023–24, Section 4.7.3, page 27

This project reviews the existing B.Tech Artificial Intelligence and Machine Learning curriculum and proposes improvements to strengthen practical learning, industry readiness, software engineering skills, and responsible AI development.

The analysis considers the programme's semester-wise course structure, selected industry job descriptions, AI-assisted learning exercises, and a proposed practical laboratory.

The recommendations are academic proposals. They have not been approved by ICFAI Tech or validated through faculty consultation.

## 2. Objectives

The objectives of this curriculum audit are to:

1. Map existing courses and credits across eight semesters.
2. Identify foundational subjects that should be retained.
3. Recommend updates to courses requiring stronger practical coverage.
4. Identify specialized content that could be reduced or reorganized.
5. Introduce modern AI engineering topics without unnecessarily increasing workload.
6. Compare the curriculum with three real, dated industry job descriptions.
7. Design and evaluate five AI-assisted learning exercises.
8. Propose a practical laboratory based on the workflow investigation in Task 1.
9. Estimate the credit impact of the proposed changes.
10. Document evidence gaps, limitations, and requirements for academic validation.

## 3. Existing Curriculum Analysis

The existing curriculum includes subjects covering mathematics, programming, data structures, algorithms, databases, artificial intelligence, machine learning, deep learning, and specialized engineering topics.

The semester-wise transcription is available in `official_curriculum.csv`.

### 3.1 Recorded Credit Distribution

| Semester | Transcribed Course Credits |
|---|---:|
| Semester I | 22 |
| Semester II | 22 |
| Semester III | 24 |
| Semester IV | 24 |
| Semester V | 24 |
| Semester VI | 19 |
| Semester VII | Individual allocations unresolved |
| Semester VIII | Individual allocations unresolved |
| **Recorded total for I–VI** | **135** |

The handbook page contains discrepancies between the visible course-credit sums, printed semester totals, and displayed programme total.

The printed semester totals add to 159, whereas the handbook's displayed programme total is 161. The transcribed course credits for Semesters I–VI add to 135, which also differs from the corresponding printed semester totals.

These discrepancies require confirmation against the applicable official curriculum regulations and detailed course scheme.

Therefore, this report does not claim that the complete eight-semester credit structure has been independently verified.

## 4. Curriculum Redesign Methodology

The curriculum was reviewed using four categories:

**KEEP:** Retain subjects that provide essential technical and mathematical foundations.

**UPDATE:** Improve existing courses through revised topics, laboratory work, and assessment methods.

**REDUCE:** Reorganize selected specialized material to create room for broader AI engineering competencies.

**ADD:** Introduce new topics that address identified practical or industry skill gaps.

Recommendations were informed by the course list and the three job descriptions documented in `job_comparison.md`.

The course titles alone do not establish everything currently taught. Detailed syllabi would be required to confirm whether particular topics are genuinely absent.

## 5. KEEP Recommendations

### 5.1 Computer Programming

**Recommendation:** KEEP.

Programming is a fundamental requirement for AI development, software engineering, data processing, and automation.

Students should retain a strong foundation in programming logic, debugging, functions, and problem-solving.

### 5.2 Data Structures

**Recommendation:** KEEP.

Data structures support efficient software development and computational problem-solving.

Lists, stacks, queues, trees, graphs, and hashing are important for technical interviews and implementation work.

### 5.3 Design and Analysis of Algorithms

**Recommendation:** KEEP.

Algorithm analysis develops understanding of computational efficiency, complexity, and scalable problem-solving.

These skills remain relevant to software engineering and large-scale data processing.

### 5.4 Mathematical Foundations

**Recommendation:** KEEP.

Linear algebra, probability, statistics, and calculus provide mathematical foundations for optimization, machine learning, and neural networks.

Reducing these foundations could weaken students' ability to understand AI methods beyond using libraries.

## 6. UPDATE Recommendations

### 6.1 Database Management Systems

**Recommendation:** UPDATE.

Introduce additional practical activities involving SQL optimization, data validation, and basic data pipeline design.

**Reason:** AI systems depend on reliable data storage, retrieval, and preparation.

### 6.2 Artificial Intelligence

**Recommendation:** UPDATE.

Add exercises involving search strategy evaluation, explainability, and responsible use of AI systems.

**Reason:** Students should learn to evaluate AI behavior rather than only implement algorithms.

### 6.3 Data Science

**Recommendation:** UPDATE.

Introduce reproducible notebooks, dataset documentation, and automated data-quality checks.

**Reason:** Reproducibility and data quality are essential for reliable analysis.

### 6.4 Machine Learning

**Recommendation:** UPDATE.

Strengthen practical work on train/test separation, cross-validation, data leakage, model comparison, and experiment tracking.

**Reason:** Correct evaluation is essential for developing trustworthy machine learning models.

### 6.5 Data Wrangling and Visualization

**Recommendation:** UPDATE.

Add automated data-cleaning workflows, validation rules, and interactive dashboards.

**Reason:** Practical data preparation and communication are important parts of AI development.

### 6.6 Deep Learning

**Recommendation:** UPDATE.

Include practical exposure to pretrained models, transfer learning, model optimization, and introductory large language model workflows.

**Reason:** Modern AI engineering frequently involves adapting and evaluating existing models.

### 6.7 Big Data Systems

**Recommendation:** UPDATE.

Strengthen practical coverage of distributed data processing and scalable pipelines.

**Reason:** Real-world machine learning applications may require processing data beyond a single-machine workflow.

### 6.8 Special Project

**Recommendation:** UPDATE.

Require project submissions to include automated tests, version control, documentation, reproducibility instructions, and a deployment or demonstration plan.

**Reason:** Students benefit from demonstrating complete software engineering workflows.

## 7. REDUCE Recommendations

### 7.1 Blockchain Technology

**Recommendation:** REDUCE selected compulsory content from three credits to two credits, subject to academic review.

**Reason:** Advanced blockchain specialization may be more suitable as elective content for students pursuing AI-focused careers.

The proposal does not recommend removing essential distributed-systems concepts.

### 7.2 Autonomous Vehicles

**Recommendation:** REDUCE selected specialized content from three credits to two credits, subject to academic review.

**Reason:** Some application-specific material could be reorganized to create room for general AI deployment skills.

The proposal should preserve important learning outcomes related to perception, control, and safety.

## 8. ADD Recommendations

### 8.1 Responsible AI and Model Evaluation

**Recommendation:** ADD one credit.

Proposed topics include:

- Fairness and bias evaluation
- Data privacy
- Model explainability
- Model documentation
- Reliability and limitations
- Responsible deployment decisions

**Reason:** Students should understand the risks and responsibilities associated with AI systems.

### 8.2 MLOps and Model Deployment

**Recommendation:** ADD one credit.

Proposed topics include:

- Model versioning
- Reproducible pipelines
- Model serving
- Basic deployment
- Monitoring
- Testing and maintenance

**Reason:** Building an accurate model is only one stage of delivering a useful AI application.

## 9. Proposed Credit Redistribution

The provisional proposal makes the following changes:

| Course or Topic | Existing Credits | Proposed Credits | Change |
|---|---:|---:|---:|
| Blockchain Technology | 3 | 2 | −1 |
| Responsible AI and Model Evaluation | 0 | 1 | +1 |
| Autonomous Vehicles | 3 | 2 | −1 |
| MLOps and Model Deployment | 0 | 1 | +1 |
| **Total** | **6** | **6** | **0** |

The proposed redistribution is credit-neutral within these four entries.

Other recommended course updates retain their existing credit allocations.

### 9.1 Estimated Credit Impact

The change register identifies 27 affected credits.

Using the 135 recorded credits across Semesters I–VI:

**Affected percentage = (27 ÷ 135) × 100 = 20%**

This calculation is limited to the six-semester transcription.

It must not be presented as a verified 20% change to the complete eight-semester programme.

The full proposed change register is available in `proposed_curriculum.csv`.

## 10. Industry Job Description Comparison

Three dated Amazon job descriptions were selected to identify relevant technical skills.

### Job 1 — Applied Scientist II, Amazon Music

**Reported posting date:** 22 October 2026.

Relevant skills include programming, machine learning, experimentation, data processing, and model-serving systems.

**Curriculum implication:** Strengthen practical ML experimentation and deployment-oriented activities.

### Job 2 — Senior Applied Scientist, Buyer Risk Prevention

**Reported posting date:** 22 October 2026.

Relevant skills include programming, machine learning frameworks, neural networks, and large-scale processing.

**Curriculum implication:** Improve practical Deep Learning and Big Data Systems assignments.

### Job 3 — Applied Scientist I

**Reported posting date:** 17 May 2026.

Relevant skills include programming, machine learning, deep learning, and model inference.

**Curriculum implication:** Add modern model evaluation and efficient inference exercises.

### Comparison Summary

| Industry Skill | Existing Curriculum | Proposed Action |
|---|---|---|
| Programming | Computer Programming | KEEP |
| Data structures | Data Structures | KEEP |
| Algorithms | Design and Analysis of Algorithms | KEEP |
| Machine learning | Machine Learning | UPDATE |
| Deep learning | Deep Learning | UPDATE |
| Large-scale processing | Big Data Systems | UPDATE |
| Model deployment | No dedicated course identified | ADD |
| Responsible AI | Dedicated coverage not established | ADD |
| Software testing | Coverage requires detailed syllabus verification | UPDATE project assessment |

The complete comparison, including job identifiers and source links, is available in `job_comparison.md`.

**Limitation:** All three job descriptions come from one employer, and some describe experienced roles. They provide selected industry evidence rather than a representative survey of graduate hiring requirements.

## 11. AI-Assisted Exercise Evaluation

Five AI-assisted learning exercises were designed for existing courses.

| Course | Proposed Exercise | Verification |
|---|---|---|
| Computer Programming | Find the maximum element in a list | Python test cases |
| Data Structures | Implement a stack | Operation and boundary tests |
| Database Management Systems | Write an SQL aggregation query | SQLite test |
| Machine Learning | Explain and prevent data leakage | Reference logic check |
| Deep Learning | Calculate convolution output dimensions | Mathematical verification |

The reference verification script was executed on 24 October 2026.

**Result: 5/5 reference tests passed.**

The exercise descriptions and expected outcomes are recorded in `ai_exercises.md`.

The test script is available in `test_ai_exercises.py`.

### Evaluation Limitation

These tests verify reference implementations and expected outcomes.

They do not constitute a completed evaluation of five captured AI-generated responses.

To complete that requirement, actual AI responses should be recorded, independently checked, and evaluated for accuracy, clarity, and potential errors.

## 12. Proposed Practical Laboratory

### Laboratory Title

**College Lab Booking and Approval System**

### Proposed Host Course

Database Management Systems.

### Related Courses

Computer Programming, Web Enabled Technologies, and Special Project.

### Learning Objectives

Students should be able to:

1. Design a relational database.
2. Implement booking request operations.
3. Validate required information.
4. Detect duplicate bookings.
5. Enforce approval permissions.
6. Test exception-handling scenarios.
7. Document recovery procedures.

### Proposed Activities

**Session 1:** Database design and SQL schema.

**Session 2:** Booking workflow implementation.

**Session 3:** Testing of normal and exceptional requests.

**Session 4:** Documentation, review, and demonstration.

The laboratory uses the hypothetical workflow developed in Task 1.

No real student data is required.

The detailed laboratory proposal is available in `lab_design.md`.

## 13. Expected Educational Benefits

The proposed curriculum changes aim to improve:

- Practical programming ability
- Reproducible AI experimentation
- Data engineering skills
- Model evaluation
- Deployment readiness
- Responsible AI awareness
- Software testing
- Technical documentation
- Project-based learning

These are expected educational benefits rather than measured outcomes.

## 14. Validation Requirements

Before implementing the proposed changes, the following activities would be necessary:

1. Confirm the applicable official regulations and curriculum version.
2. Resolve the discrepancies in programme credits.
3. Review detailed course syllabi.
4. Obtain faculty feedback on the proposed credit redistribution.
5. Consult graduates about practical skill requirements.
6. Compare job descriptions from additional employers.
7. Pilot the proposed laboratory.
8. Collect and evaluate actual AI-generated exercise responses.

No faculty approval, graduate consultation, or classroom pilot is claimed in this report.

## 15. Limitations

This analysis has the following limitations:

1. The available handbook page contains unresolved credit discrepancies.
2. Individual final-year credit allocations are incomplete in the transcription.
3. The proposed curriculum CSV is a change register rather than a complete replacement curriculum.
4. The credit-impact percentage uses only the recorded Semesters I–VI baseline.
5. The industry comparison covers three postings from one employer.
6. Detailed course-level syllabus content has not been fully verified.
7. No faculty or graduate validation has been recorded.
8. The AI exercise tests do not evaluate actual AI-generated responses.
9. The proposed laboratory has not been implemented in a classroom.

## 16. Conclusion

The B.Tech Artificial Intelligence and Machine Learning curriculum includes important foundations in programming, mathematics, algorithms, databases, machine learning, and deep learning.

The proposed redesign retains these foundations while strengthening practical AI development, model deployment, responsible AI, data processing, and software testing.

A provisional credit-neutral redistribution introduces Responsible AI and MLOps content without increasing the total credits in the affected course entries.

The analysis provides a structured basis for curriculum discussion, but the final recommendations require verification against the official regulations, detailed syllabus, and relevant academic feedback.