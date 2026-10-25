"""Temperature conversion (Feature B)."""

import math

UNITS = ("c", "f", "k")

ABSOLUTE_ZERO_C = -273.15


def _to_celsius(value, unit):
    if unit == "c":
        return value
    if unit == "f":
        return (value - 32) * 5 / 9
    return value - 273.15  # kelvin


def _from_celsius(celsius, unit):
    if unit == "c":
        return celsius
    if unit == "f":
        return celsius * 9 / 5 + 32
    return celsius + 273.15  # kelvin


def _normalise_unit(unit):
    if not isinstance(unit, str):
        raise TypeError("unit must be a string")
    key = unit.strip().lower().lstrip("°")
    if key not in UNITS:
        raise ValueError(
            f"Unknown temperature unit '{unit}'. Supported: C, F, K"
        )
    return key


def convert(value, from_unit, to_unit):
    """Convert a temperature between Celsius, Fahrenheit and Kelvin.

    Raises TypeError for non-numeric values and ValueError for unknown units,
    non-finite numbers, or temperatures below absolute zero.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be a number")
    if not math.isfinite(value):
        raise ValueError("value must be a finite number")

    source = _normalise_unit(from_unit)
    target = _normalise_unit(to_unit)

    celsius = _to_celsius(value, source)
    # Tolerate tiny floating point error right at absolute zero.
    if celsius < ABSOLUTE_ZERO_C - 1e-9:
        raise ValueError("temperature cannot be below absolute zero")

    return _from_celsius(celsius, target)
