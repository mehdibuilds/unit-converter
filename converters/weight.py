"""Weight (mass) conversion (Feature C)."""

import math

# Size of each unit expressed in kilograms.
UNITS = {
    "mg": 0.000001,
    "g": 0.001,
    "kg": 1.0,
    "t": 1000.0,
    "oz": 0.028349523125,
    "lb": 0.45359237,
    "st": 6.35029318,
}


def _unit_factor(unit):
    """Look up a unit symbol (case-insensitive) and return its size in kg."""
    if not isinstance(unit, str):
        raise TypeError("unit must be a string")
    key = unit.strip().lower()
    if key not in UNITS:
        raise ValueError(
            f"Unknown weight unit '{unit}'. Supported: {', '.join(UNITS)}"
        )
    return UNITS[key]


def convert(value, from_unit, to_unit):
    """Convert a weight from one unit to another.

    Raises TypeError for non-numeric values and ValueError for unknown units,
    non-finite numbers, or negative weights.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be a number")
    if not math.isfinite(value):
        raise ValueError("value must be a finite number")
    if value < 0:
        raise ValueError("weight cannot be negative")

    kilograms = value * _unit_factor(from_unit)
    return kilograms / _unit_factor(to_unit)
