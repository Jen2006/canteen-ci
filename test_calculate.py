import pytest
from calculate import calculate_total


def test_amount_below_300():
    assert calculate_total(200) == 210.00


def test_amount_equal_to_300():
    assert calculate_total(300) == 315.00


def test_amount_above_300():
    assert calculate_total(400) == 400.00


def test_zero_amount():
    assert calculate_total(0) == 0.00


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_total(-100)