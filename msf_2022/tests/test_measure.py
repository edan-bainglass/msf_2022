"""
Tests related to the measure module.
"""

import pytest
import numpy as np
import msf_2022


def test_calculate_distance() -> None:

    r1 = np.array([0, 2, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1.0

    calculated_distance = msf_2022.calculate_distance(r1, r2)

    assert calculated_distance == expected_distance, "Unexpected calculated distance"


@pytest.mark.parametrize(
    "p1, p2, p3, expected_angle",
    [
        (
            np.array([np.sqrt(2) / 2, np.sqrt(2) / 2, 0]),
            np.array([0, 0, 0]),
            np.array([1, 0, 0]),
            45,
        ),
        (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
        (
            np.array([np.sqrt(3) / 2, (1 / 2), 0]),
            np.array([0, 0, 0]),
            np.array([1, 0, 0]),
            30,
        ),
    ],
)
def test_calculate_angle_many(p1, p2, p3, expected_angle):

    calculated_angle = msf_2022.calculate_angle(p1, p2, p3, degrees=True)

    assert expected_angle == pytest.approx(
        calculated_angle
    ), f"{calculated_angle} {expected_angle}"
