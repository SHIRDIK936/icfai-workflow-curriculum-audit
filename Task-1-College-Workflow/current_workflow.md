# Current Laboratory Booking Workflow

## Evidence Status

This is a hypothetical manual workflow developed for
academic analysis.

No actual ICFAI laboratory booking process was observed.
All steps and roles are assumptions.

## Current Process

```mermaid
flowchart TD
    A([Start]) --> B[Student needs laboratory]
    B --> C[Student prepares booking request]
    C --> D[Submit request to faculty]
    D --> E[Faculty checks information]
    E --> F{Information complete?}

    F -->|No| G[Return for correction]
    G --> C

    F -->|Yes| H[Check laboratory availability]
    H --> I{Slot available?}

    I -->|No| J[Suggest alternative slot]
    J --> C

    I -->|Yes| K[Authorized faculty reviews request]
    K --> L{Approved?}

    L -->|No| M[Communicate rejection]
    L -->|Yes| N[Communicate approval]

    M --> O([End])
    N --> O
```

## Assumed Roles

| Role | Responsibility |
|---|---|
| Student | Submits booking request |
| Faculty coordinator | Checks request details |
| Laboratory coordinator | Checks laboratory availability |
| Authorized approver | Approves or rejects requests |

## Potential Problems

1. Missing request information may cause rework.
2. Duplicate requests may increase processing effort.
3. Availability checks may require manual coordination.
4. Students may need to ask for status updates.
5. Approval records may be difficult to consolidate.

These are hypothetical risks, not verified ICFAI problems.