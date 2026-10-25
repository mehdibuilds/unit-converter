"""Length conversion (Feature A)."""

import math

# Size of each unit expressed in metres.
UNITS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
}


def _unit_factor(unit):
    """Look up a unit symbol (case-insensitive) and return its size in metres."""
    if not isinstance(unit, str):
        raise TypeError("unit must be a string")
    key = unit.strip().lower()
    if key not in UNITS:
        raise ValueError(
            f"Unknown length unit '{unit}'. Supported: {', '.join(UNITS)}"
        )
    return UNITS[key]


def convert(value, from_unit, to_unit):
    """Convert a length from one unit to another.

    Raises TypeError for non-numeric values and ValueError for unknown units
    or non-finite numbers (NaN / infinity).
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be a number")
    if not math.isfinite(value):
        raise ValueError("value must be a finite number")

    metres = value * _unit_factor(from_unit)
    return metres / _unit_factor(to_unit)
