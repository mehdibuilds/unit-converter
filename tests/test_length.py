import pytest

from converters.length import convert


def test_kilometres_to_metres():
    assert convert(1.5, "km", "m") == pytest.approx(1500)


def test_miles_to_kilometres():
    assert convert(1, "mi", "km") == pytest.approx(1.609344)


def test_zero_length_and_same_unit_edge_cases():
    assert convert(0, "ft", "m") == 0
    assert convert(42, "cm", "cm") == pytest.approx(42)


def test_unit_names_are_case_insensitive():
    assert convert(12, "IN", "Ft") == pytest.approx(1)


def test_unknown_unit_raises_value_error():
    with pytest.raises(ValueError):
        convert(5, "parsec", "m")


def test_non_numeric_value_raises_type_error():
    with pytest.raises(TypeError):
        convert("ten", "m", "km")
