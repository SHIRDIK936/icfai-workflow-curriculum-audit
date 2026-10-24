# Proposed Practical Lab: College Lab Booking and Approval System

## 1. Lab Information

**Institution:** ICFAI Tech, Hyderabad  
**Programme:** B.Tech Artificial Intelligence and Machine Learning  
**Admission batch:** 2023–2027  
**Prepared:** 24 October 2026

**Proposed host course:** Database Management Systems  
**Related courses:** Computer Programming, Web Enabled Technologies, and Special Project

**Lab title:** Design and Test a College Lab Booking and Approval System

**Suggested duration:** Four laboratory sessions of two hours each.

## 2. Problem Statement

College laboratory bookings may require checking availability, verifying request details, obtaining authorization, and notifying the requester.

This lab uses a hypothetical workflow developed in Task 1. It does not claim that the proposed process represents an observed or officially approved ICFAI procedure.

Students will design a small prototype that records booking requests, prevents duplicate bookings, and enforces approval rules.

## 3. Learning Outcomes

After completing this lab, students should be able to:

1. Design a relational database for a booking workflow.
2. Implement basic create, read, and update operations.
3. Define workflow states and valid transitions.
4. Enforce role-based approval permissions.
5. Test normal and exceptional scenarios.
6. Document failures and recovery procedures.

## 4. Proposed System Inputs

Each booking request contains:

- Request ID
- Laboratory ID
- Requested date
- Start time
- End time
- Purpose
- Requester ID
- Request status

Synthetic identifiers must be used during classroom testing.

## 5. Workflow States

The proposed workflow uses these states:

`SUBMITTED → UNDER_REVIEW → APPROVED → COMPLETED`

Alternative states include:

- `NEEDS_INFORMATION`
- `REJECTED`
- `CANCELLED`
- `FAILED`

Only an authorized approver may move a request into `APPROVED`.

## 6. Laboratory Activities

### Session 1 — Database Design

Students design tables for:

- Laboratories
- Booking requests
- Users and roles
- Approval history

**Deliverable:** Entity-relationship diagram and SQL schema.

### Session 2 — Workflow Implementation

Students implement:

- Booking submission
- Required-field validation
- Booking conflict detection
- Request status updates
- Approval authorization

**Deliverable:** Working command-line or web-based prototype.

### Session 3 — Testing

Students test five synthetic scenarios:

| Test | Expected result |
|---|---|
| Normal booking | Valid request progresses to approval |
| Missing information | Request moves to `NEEDS_INFORMATION` |
| Duplicate booking | Conflicting booking is rejected or flagged |
| Unauthorized approval | Approval is denied |
| Failed processing step | Failure is recorded and recovery is available |

**Deliverable:** Test script and test-results table.

### Session 4 — Review and Documentation

Students document:

- Workflow diagram
- Database design
- Test evidence
- Known limitations
- Recovery procedure
- Suggestions for future improvement

**Deliverable:** Short technical report and demonstration.

## 7. Assessment Rubric

| Criterion | Marks |
|---|---:|
| Database design | 20 |
| Workflow implementation | 25 |
| Input validation and authorization | 20 |
| Testing and exception handling | 20 |
| Documentation and demonstration | 15 |
| **Total** | **100** |

## 8. AI-Assisted Learning Policy

Students may use AI tools to explain database concepts, suggest test cases, or review code.

Students must disclose AI assistance, independently test generated code, and explain their implementation.

AI-generated output without verification should not receive full credit.

## 9. Fallback and Recovery

If the prototype becomes unavailable, students should retain synthetic requests in a local CSV file.

After service recovery, requests should be revalidated before import to prevent duplicate or unauthorized bookings.

## 10. Expected Benefits

This lab connects database concepts with software engineering, access control, workflow design, and testing.

It also demonstrates how a small institutional problem can become a practical learning exercise.

## 11. Limitations

The lab is a proposed teaching activity, not an implemented institutional system.

No real student information is required. The proposed workflow has not been approved by ICFAI staff.

The five Task 1 synthetic tests provide preliminary examples but do not establish production reliability or security.