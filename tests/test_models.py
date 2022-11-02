"""Tests for statistics functions within the Model layer."""

import numpy.testing as npt
import pytest

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4])
    ]
)
def test_daily_mean(test, expected):
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test), expected)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2])
    ]
)
def test_daily_min(test, expected):
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_min

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test), expected)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [5, 6])
    ]
)
def test_daily_max(test, expected):
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_max

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test), expected)


def test_daily_min_error():
    """Test that error for string."""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['abd', 'ads'], ['asd', 'auhs']])

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1,2,3], [4,5,6], [7,8,9]],
        [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]])
    ]
)
def test_patient_normalise(test, expected):

    import numpy as np
    from inflammaton.models import patient_normalise
    npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)