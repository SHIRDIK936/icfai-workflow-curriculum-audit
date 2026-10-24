from datetime import datetime

requests = {}
reservations = set()
audit_log = []


def record_event(request_id, event):
    audit_log.append({
        "request_id": request_id,
        "event": event,
        "timestamp": datetime.now().isoformat()
    })


def submit_request(request_id, student, lab, slot, purpose):
    if not all([student, lab, slot, purpose]):
        record_event(request_id, "NEEDS_CORRECTION")
        return "NEEDS_CORRECTION"

    for existing in requests.values():
        if (
            existing["student"] == student
            and existing["lab"] == lab
            and existing["slot"] == slot
        ):
            record_event(request_id, "DUPLICATE")
            return "DUPLICATE"

    requests[request_id] = {
        "student": student,
        "lab": lab,
        "slot": slot,
        "purpose": purpose,
        "status": "PENDING_APPROVAL"
    }

    record_event(request_id, "PENDING_APPROVAL")
    return "PENDING_APPROVAL"


def approve_request(request_id, role, simulate_failure=False):
    if role != "AUTHORIZED_FACULTY":
        record_event(request_id, "ACCESS_DENIED")
        return "ACCESS_DENIED"

    request = requests.get(request_id)

    if request is None:
        return "NOT_FOUND"

    if request["status"] != "PENDING_APPROVAL":
        return "INVALID_STATE"

    reservation_key = (request["lab"], request["slot"])

    if reservation_key in reservations:
        request["status"] = "CONFLICT"
        record_event(request_id, "CONFLICT")
        return "CONFLICT"

    if simulate_failure:
        request["status"] = "RECOVERY_REQUIRED"
        record_event(request_id, "RECOVERY_REQUIRED")
        return "RECOVERY_REQUIRED"

    reservations.add(reservation_key)
    request["status"] = "APPROVED"
    record_event(request_id, "APPROVED")
    return "APPROVED"


def run_tests():
    tests = []

    # TC01: Normal request
    result = submit_request(
        "REQ001", "STUDENT_A", "LAB-A",
        "10:00-11:00", "Project work"
    )
    tests.append(("TC01", result == "PENDING_APPROVAL"))

    # TC02: Missing information
    result = submit_request(
        "REQ002", "STUDENT_B", "LAB-A",
        "11:00-12:00", ""
    )
    tests.append(("TC02", result == "NEEDS_CORRECTION"))

    # TC03: Duplicate request
    result = submit_request(
        "REQ003", "STUDENT_A", "LAB-A",
        "10:00-11:00", "Project work"
    )
    tests.append(("TC03", result == "DUPLICATE"))

    # TC04: Unauthorized approval
    result = approve_request("REQ001", "STUDENT")
    tests.append(("TC04", result == "ACCESS_DENIED"))

    # TC05: Failed reservation
    result = approve_request(
        "REQ001",
        "AUTHORIZED_FACULTY",
        simulate_failure=True
    )
    tests.append(("TC05", result == "RECOVERY_REQUIRED"))

    print("\nLAB BOOKING WORKFLOW TEST RESULTS")
    print("-" * 40)

    for test_id, passed in tests:
        print(f"{test_id}: {'PASS' if passed else 'FAIL'}")

    print("-" * 40)
    print(f"Passed: {sum(p for _, p in tests)}/{len(tests)}")


if __name__ == "__main__":
    run_tests()