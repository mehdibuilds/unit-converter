import pytest

from converters.temperature import convert


def test_celsius_to_fahrenheit():
    assert convert(100, "c", "f") == pytest.approx(212)


def test_fahrenheit_to_kelvin():
    assert convert(32, "F", "K") == pytest.approx(273.15)


def test_absolute_zero_is_allowed_boundary():
    assert convert(0, "k", "c") == pytest.approx(-273.15)
    assert convert(-273.15, "c", "k") == pytest.approx(0)


def test_below_absolute_zero_raises_value_error():
    with pytest.raises(ValueError):
        convert(-1, "k", "c")


def test_unknown_unit_raises_value_error():
    with pytest.raises(ValueError):
        convert(20, "c", "rankine")


def test_nan_is_rejected():
    with pytest.raises(ValueError):
        convert(float("nan"), "c", "f")
