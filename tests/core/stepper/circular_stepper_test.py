import pytest

from core.stepper.circular_stepper import CircularStepper
from core.stepper import Stepper


@pytest.mark.parametrize(
    "minmax, value, steps, direction, expected_value",
    [
        ((0, 10), 5, 10, Stepper.DOWN, 4),
        ((0, 10), 5, 10, Stepper.UP, 6),
        ((0, 10), 1, 10, Stepper.DOWN, 0),
        ((0, 10), 9, 10, Stepper.UP, 10),
        ((0, 10), 0, 10, Stepper.DOWN, 10),
        ((0, 10), 10, 10, Stepper.UP, 0),
        ((0, 10), -1, 10, Stepper.DOWN, 9),
        ((0, 10), 11, 10, Stepper.UP, 1),
        ((0, 10), 6, 5, Stepper.DOWN, 4),
        ((0, 10), 4, 5, Stepper.UP, 6),
    ],
)
def test_minmax_stepper(minmax, value, steps, direction, expected_value):
    stepper = CircularStepper(*minmax, steps)

    # SUT
    new_value, _ = stepper.step(value, direction)

    # Checks
    assert new_value == expected_value
