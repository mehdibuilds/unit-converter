import pytest

from converters.weight import convert


def test_kilograms_to_pounds():
    assert convert(1, "kg", "lb") == pytest.approx(2.20462, rel=1e-4)


def test_grams_to_ounces():
    assert convert(100, "g", "oz") == pytest.approx(3.5274, rel=1e-4)


def test_zero_weight_edge_case():
    assert convert(0, "t", "mg") == 0


def test_negative_weight_raises_value_error():
    with pytest.raises(ValueError):
        convert(-5, "kg", "g")


def test_unknown_unit_raises_value_error():
    with pytest.raises(ValueError):
        convert(5, "kg", "furlong")


def test_boolean_value_is_rejected():
    with pytest.raises(TypeError):
        convert(True, "kg", "g")
