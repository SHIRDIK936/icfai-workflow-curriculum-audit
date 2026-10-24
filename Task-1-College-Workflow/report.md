# Task 1: College Lab Booking and Approval System

## 1. Introduction

This project explores a hypothetical laboratory booking
workflow at ICFAI Tech, Hyderabad.

## 2. Evidence Boundary

No real college process was observed or confirmed.
No staff interviews were conducted.

The workflow, processing times and request volumes
are assumptions for academic evaluation.

## 3. Hypothetical Current Workflow

1. Student prepares laboratory booking request.
2. Student submits request to faculty.
3. Faculty checks request information.
4. Laboratory availability is checked.
5. Authorized approver accepts or rejects.
6. Decision is communicated to the student.

## 4. Potential Problems

- Manual processing delays
- Duplicate booking requests
- Missing request information
- Limited request tracking
- Additional administrative work

These are hypothetical risks, not observed ICFAI problems.

## 5. Proposed Digital Workflow

1. Student opens booking portal.
2. Student selects laboratory and time slot.
3. System validates required information.
4. System checks for duplicate requests.
5. Authorized faculty reviews the request.
6. Faculty approves or rejects.
7. System records the decision and audit event.

## 6. Synthetic Test Cases

TC01: Normal request
Expected: Sent for approval.

TC02: Missing information
Expected: Request returned for correction.

TC03: Duplicate request
Expected: Duplicate flagged.

TC04: Unauthorized approval
Expected: Action denied and logged.

TC05: System failure
Expected: Safe recovery without duplicate approval.

These are expected outcomes, not executed test results.

## 7. Preliminary Time Calculation

Assumed manual effort: 25 minutes/request.
Assumed digital effort: 8 minutes/request.
Assumed monthly volume: 100 requests.

Gross savings:
(25 - 8) * 100 = 1700 minutes/month.

Gross savings = 28.33 hours/month.

Review, support, rework and implementation effort
must be deducted before reporting net savings.

## 8. Limitations

- No field observations
- No measured processing times
- No verified request volume
- No institutional system access
- No production implementation

This is a hypothetical academic case study.
