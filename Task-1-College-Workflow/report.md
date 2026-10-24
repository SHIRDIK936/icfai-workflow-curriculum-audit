# TASK 1: COLLEGE LAB BOOKING AND APPROVAL SYSTEM

## 1. Introduction

**Institution:** ICFAI Tech, Hyderabad  
**Programme:** B.Tech Artificial Intelligence and Machine Learning  
**Admission Batch:** 2023–2027  
**Study Date:** 24 October 2026  
**Process Selected:** College Laboratory Booking and Approval System

This project examines a hypothetical college laboratory booking and approval workflow.

The purpose is to understand how a small administrative process can be analyzed, redesigned, tested, and evaluated for efficiency.

The proposed solution focuses on reducing manual work, improving request tracking, preventing duplicate bookings, and ensuring that only authorized personnel approve requests.

**Evidence boundary:** This is a hypothetical academic case study. No real ICFAI laboratory booking process was observed or verified, and no staff interviews or institutional approvals were obtained.

## 2. Problem Statement

A laboratory booking process may involve students submitting requests, faculty reviewing them, checking availability, and communicating approval decisions.

When these activities are performed manually, potential difficulties include:

1. Delays caused by multiple handoffs.
2. Incomplete booking requests.
3. Duplicate requests for the same laboratory and time.
4. Limited visibility into request status.
5. Additional administrative effort.
6. Difficulty tracking approvals and exceptions.

These are possible workflow risks, not confirmed problems at ICFAI Tech.

The objective is to design a structured process that improves transparency, accountability, and exception handling.

## 3. Evidence Collection and Classification

The project uses three evidence classifications.

### 3.1 Observed Facts

No institutional workflow observations were collected.

The existence of ICFAI Tech and its academic programme provides background context but does not verify the hypothetical booking process.

### 3.2 Assumptions

The following assumptions are used:

- Students may request access to laboratories.
- Faculty or designated staff review booking requests.
- Laboratory availability must be checked.
- An authorized person makes the final approval decision.
- A laboratory may receive multiple requests for the same time slot.

These assumptions are used to construct a testable model.

### 3.3 Estimates

The following numerical estimates are used for evaluation:

| Parameter | Estimated value |
|---|---:|
| Monthly booking requests | 100 |
| Manual processing time per request | 25 minutes |
| Proposed digital processing time per request | 8 minutes |
| Monthly reduction in rework | 175 minutes |
| Monthly review and support effort | 180 minutes |
| One-time implementation effort | 60 hours |

None of these values represents measured institutional performance.

A dated evidence log is maintained in `evidence_log.csv`.

## 4. Hypothetical Current Workflow

The current-state model contains the following steps.

| Step | Activity | Responsible role | Handoff |
|---|---|---|---|
| 1 | Prepare laboratory booking request | Student | Student → Faculty |
| 2 | Submit request | Student | Faculty receives request |
| 3 | Check required information | Faculty | Faculty → Lab coordinator |
| 4 | Verify laboratory availability | Lab coordinator | Coordinator → Approver |
| 5 | Approve or reject request | Authorized approver | Approver → Faculty/Student |
| 6 | Communicate decision | Faculty or coordinator | Decision → Student |

### Current-State Exceptions

**Missing information:** The request may be returned to the student for correction.

**Duplicate booking:** Multiple requests may compete for the same laboratory and time slot.

**Unavailable laboratory:** The requester may need to select a different time.

**Delayed approval:** A request may remain pending until the responsible approver responds.

**Processing failure:** Records or communication may need to be recovered manually.

These exceptions are hypothetical scenarios for analysis.

The workflow diagram is available in `current_workflow.md`.

## 5. Estimated Problem Scale

For the purpose of this case study, the laboratory is assumed to receive 100 booking requests each month.

If each request requires 25 minutes of manual administrative effort:

**Monthly manual effort = 100 × 25 = 2,500 minutes**

Therefore:

**Monthly manual effort = 41.67 hours**

This estimate illustrates the potential scale of administrative work under the stated assumptions.

It is not a measurement of actual ICFAI laboratory operations.

## 6. Proposed Digital Workflow

The proposed system introduces a centralized request form, validation, status tracking, and controlled approval.

### 6.1 Required Inputs

Each request contains:

- Unique request ID
- Requester ID
- Laboratory ID
- Booking date
- Start time
- End time
- Purpose of booking

Only synthetic identifiers are used in testing.

### 6.2 Workflow Steps

1. The student submits a booking request through a digital form.
2. The system validates mandatory fields.
3. The system checks for conflicting or duplicate requests.
4. A valid request is forwarded to the designated reviewer.
5. The authorized approver reviews the request.
6. The approver approves or rejects the booking.
7. The system records the decision and timestamp.
8. The student receives the updated request status.

### 6.3 Workflow Statuses

| Status | Meaning |
|---|---|
| SUBMITTED | Request received |
| NEEDS_INFORMATION | Required information is missing |
| UNDER_REVIEW | Awaiting authorized review |
| APPROVED | Booking approved |
| REJECTED | Booking declined |
| CANCELLED | Request cancelled |
| COMPLETED | Approved booking completed |
| FAILED | Processing error requires recovery |

### 6.4 Accountable Owner

The proposed **laboratory coordinator** is accountable for monitoring requests, handling exceptions, and ensuring that unresolved requests receive attention.

This role is proposed for the model and has not been confirmed as an existing institutional responsibility.

### 6.5 Approval Boundaries

Students may submit and view their own requests.

Faculty reviewers may verify information and recommend decisions.

Only a designated authorized approver may approve or reject requests.

Unauthorized approval attempts must be denied and recorded.

### 6.6 Duplicate Prevention

Before approval, the system checks whether an existing approved booking conflicts with the requested laboratory and time interval.

Requests that conflict with an approved booking must be flagged for review or rejected.

### 6.7 Fallback Procedure

If the digital system becomes unavailable:

1. The coordinator records new requests in a controlled temporary log.
2. Requests are marked as pending rather than automatically approved.
3. When the system is restored, pending requests are revalidated.
4. Duplicate and conflicting requests are checked again.
5. Only authorized personnel complete approvals.
6. The coordinator reconciles the temporary log with the restored system.

This is a proposed recovery procedure, not a production-tested implementation.

The proposed workflow diagram is available in `proposed_workflow.md`.

## 7. Synthetic Test Cases

Five synthetic test scenarios were prepared to evaluate the reference workflow logic.

| Test ID | Scenario | Expected result | Reference test |
|---|---|---|---|
| TC01 | Normal booking request | Request follows the valid approval path | PASS |
| TC02 | Missing information | Request requires correction | PASS |
| TC03 | Duplicate request | Duplicate is detected or flagged | PASS |
| TC04 | Unauthorized approval | Unauthorized action is denied | PASS |
| TC05 | Simulated processing failure | Failure is handled according to the test logic | PASS |

### Test Execution

The reference Python test script was executed on **24 October 2026**.

**Result: 5 out of 5 tests passed.**

The tests demonstrate that the implemented reference checks behaved as expected for the supplied synthetic inputs.

They do not prove database durability, concurrent booking safety, complete audit logging, or successful recovery from real infrastructure failures.

Supporting files:

- `test_cases.csv`
- `test_workflow.py`

## 8. Estimated Time Savings and ROI

### 8.1 Manual Processing Effort

Assumed monthly requests: 100

Assumed manual processing time: 25 minutes per request

**Manual effort = 100 × 25 = 2,500 minutes/month**

### 8.2 Proposed Digital Processing Effort

Assumed digital processing time: 8 minutes per request

**Digital effort = 100 × 8 = 800 minutes/month**

### 8.3 Gross Time Savings

**Gross savings = 2,500 − 800**

**Gross savings = 1,700 minutes/month**

### 8.4 Rework Reduction

The model assumes an additional 175 minutes per month could be saved by reducing repeated corrections and duplicate handling.

**Total estimated savings before support = 1,700 + 175**

**Total = 1,875 minutes/month**

### 8.5 Review and Support Effort

The model includes 180 minutes per month for review, support, and system administration.

**Net savings = 1,875 − 180**

**Net savings = 1,695 minutes/month**

Converting to hours:

**1,695 ÷ 60 = 28.25 hours/month**

### 8.6 Implementation Payback

Assumed one-time implementation effort: 60 hours.

**Estimated payback = 60 ÷ 28.25**

**Estimated payback ≈ 2.12 months**

### 8.7 Sensitivity Analysis

| Monthly requests | Estimated net time saved |
|---|---:|
| 50 | 12.63 hours |
| 100 | 28.25 hours |
| 150 | 43.88 hours |

These calculations are illustrative. Actual savings would depend on measured request volumes, approval times, support requirements, and implementation costs.

The detailed calculation is available in `roi_calculation.md`.

## 9. Risks and Mitigation

| Risk | Proposed mitigation |
|---|---|
| Missing information | Mandatory-field validation |
| Duplicate booking | Conflict detection |
| Unauthorized approval | Role-based authorization |
| System failure | Controlled temporary log and reconciliation |
| Incorrect status | Validated state transitions |
| Data exposure | Restricted access and minimal data collection |
| Delayed review | Assigned coordinator and pending-request monitoring |

The full discussion is provided in `risks_and_limitations.md`.

## 10. Expected Benefits

The proposed workflow may provide:

1. More consistent booking requests.
2. Better visibility into approval status.
3. Reduced duplicate submissions.
4. Clearer responsibility for pending requests.
5. Improved traceability of decisions.
6. Lower administrative effort under the assumed workload.

These benefits are anticipated outcomes, not measured improvements.

## 11. Limitations

This study has several important limitations.

1. No permission-based field investigation was conducted.
2. No real college workflow was observed.
3. No faculty or laboratory staff interviews were completed.
4. Request volume and processing times are estimates.
5. All test cases use synthetic information.
6. The system was not deployed in an institutional environment.
7. The reference tests do not establish production security or reliability.
8. The estimated time savings have not been independently validated.

The original assignment's permission-based investigation requirement therefore remains unmet.

## 12. Future Improvements

With appropriate institutional permission, the next stage could include:

- Observing the actual laboratory booking process.
- Interviewing authorized faculty and laboratory coordinators.
- Recording real processing times without collecting unnecessary personal information.
- Comparing actual workflow steps with the hypothetical model.
- Testing concurrency, audit logging, and recovery.
- Conducting a small pilot with authorized users.
- Recalculating time savings using measured data.

## 13. Conclusion

This project presents a hypothetical analysis and redesign of a College Lab Booking and Approval System.

The proposed workflow introduces structured inputs, defined statuses, accountable ownership, approval boundaries, duplicate detection, and a fallback procedure.

Five synthetic reference tests passed, and the estimated net time savings under the stated assumptions are **28.25 hours per month**.

The project demonstrates a method for analyzing and improving a small administrative workflow. However, it remains an academic simulation rather than a verified investigation of an existing ICFAI process.