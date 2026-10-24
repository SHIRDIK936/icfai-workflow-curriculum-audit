# Proposed Digital Laboratory Booking Workflow

## Proposed Solution

A centralized laboratory booking system that validates
requests and routes them to an authorized human approver.

```mermaid
flowchart TD
    A([Start]) --> B[Student opens booking portal]
    B --> C[Select laboratory and time slot]
    C --> D[Enter booking details]
    D --> E{Required information complete?}

    E -->|No| F[Request correction]
    F --> D

    E -->|Yes| G[Check duplicate requests]
    G --> H{Duplicate found?}

    H -->|Yes| I[Show existing request]
    I --> Z([End])

    H -->|No| J[Check slot availability]
    J --> K{Slot available?}

    K -->|No| L[Suggest alternative slot]
    L --> C

    K -->|Yes| M[Send to authorized approver]
    M --> N{Approval decision}

    N -->|Reject| O[Record rejection reason]
    N -->|Approve| P[Reserve slot atomically]

    P --> Q{Reservation saved?}
    Q -->|No| R[Flag recovery and notify owner]
    R --> S[Reconcile state before retry]
    S --> P

    Q -->|Yes| T[Record approval and audit event]
    O --> U[Notify student]
    T --> U
    U --> Z
```

## Required Inputs

- Synthetic requester reference
- Laboratory identifier
- Booking date
- Start time
- End time
- Purpose of booking

## Request Statuses

- DRAFT
- NEEDS_CORRECTION
- PENDING_APPROVAL
- APPROVED
- REJECTED
- CONFLICT
- RECOVERY_REQUIRED
- CANCELLED

## Approval Control

Only a designated authorized approver may approve or
reject a request.

The system must verify the approver's permissions
before accepting a decision.

## Audit Record

Each important event records:

- Request reference
- Event timestamp
- Previous status
- New status
- Action type
- Actor role
- Decision reason, when applicable

## Failure Recovery

If reservation storage fails, the request enters
RECOVERY_REQUIRED.

The accountable laboratory coordinator checks whether
a reservation was already saved before authorizing
a retry.

The system must prevent duplicate reservations.

## Technology Choice

Ordinary software rules are sufficient for:

- Required-field validation
- Duplicate detection
- Slot conflict checking
- Role-based approval
- Audit logging

Artificial intelligence is not required for the core
booking and approval process.

An AI assistant could optionally explain booking rules,
but it must not make approval decisions.