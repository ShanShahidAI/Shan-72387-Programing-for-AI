"""Automated tests for student support rules."""

from support_engine import classify_support, format_message


def run_tests():
    """Check priority boundaries and messages with assertions."""
    # Test 1: Below attendance boundary (High priority)
    assert classify_support(59.9, 90, 0) == "High priority"

    # Test 2: High missed submissions boundary (High priority)
    assert classify_support(60, 90, 4) == "High priority"

    # Test 3: Below attendance boundary (Moderate priority)
    assert classify_support(74.9, 90, 0) == "Moderate priority"

    # Test 4: Below average boundary (Moderate priority)
    assert classify_support(75, 59.9, 0) == "Moderate priority"

    # Test 5: Moderate missed submissions boundary (Moderate priority)
    assert classify_support(90, 90, 2) == "Moderate priority"

    # Test 6: Minimum routine values (Routine monitoring)
    assert classify_support(75, 60, 1) == "Routine monitoring"

    # Test 7: Maximum valid values (Routine monitoring)
    assert classify_support(100, 100, 0) == "Routine monitoring"

    # Message tests
    assert (
        format_message("High priority") == "Immediate academic support is recommended."
    )
    assert (
        format_message("Moderate priority")
        == "Monitor progress and provide targeted guidance."
    )
    assert format_message("Routine monitoring") == "Continue routine monitoring."

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
