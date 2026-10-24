# Task 1 — Risks, Limitations and Design Decisions

## 1. Project Scope

This project investigates a hypothetical laboratory booking
workflow at ICFAI Tech, Hyderabad.

No actual institutional workflow was observed or verified.

## 2. Risks and Mitigations

| Risk | Potential Impact | Mitigation |
|---|---|---|
| Unauthorized approval | Improper laboratory access | Role-based access control |
| Duplicate booking | Conflicting reservations | Duplicate and conflict checks |
| Missing information | Processing delays | Required-field validation |
| Database failure | Inconsistent booking status | Recovery state and reconciliation |
| Incorrect availability | Double booking | Atomic reservation operation |
| Low student adoption | Reduced time savings | Simple interface and training |
| System downtime | Booking interruptions | Authorized manual fallback |
| Incorrect assumptions | Misleading ROI | Validate timings before deployment |

## 3. Accountable Owner

Proposed accountable owner:
Laboratory Coordinator.

This is a proposed role, not a verified ICFAI assignment.

## 4. Approval Boundary

The system validates requests but does not approve them.

Only designated authorized faculty may approve or reject
laboratory booking requests.

## 5. Manual Fallback

During a system outage:

1. The laboratory coordinator records requests in a
   controlled temporary register.
2. An authorized approver makes the decision.
3. The coordinator checks for existing reservations.
4. Requests are reconciled when the system recovers.
5. Duplicate reservations are prevented.

## 6. Remaining Unknowns

- Actual booking request volume
- Existing institutional booking procedures
- Faculty approval responsibilities
- Real processing times
- Actual correction and rejection rates
- Laboratory scheduling constraints
- Software maintenance requirements

## 7. Evidence That Could Change the Design

If future authorized observation shows that laboratories
already use an efficient digital booking system with
minimal delays, the proposed replacement system should
be abandoned.

The project should instead investigate specific remaining
problems, if any.

## 8. Limitations of Synthetic Testing

The five Python tests passed in an in-memory simulation.

They do not establish:

- Real-world effectiveness
- Database transaction safety
- Concurrent booking protection
- Recovery after an actual outage
- Institutional acceptance

Additional testing would be required before deployment.

## 9. Conclusion

The proposed system demonstrates a possible improvement
to a hypothetical manual workflow.

Its effectiveness and estimated time savings remain
unverified until authorized field evidence is available.