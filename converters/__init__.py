"""Unit converter package.

Each category (length, temperature, weight) lives in its own module and
exposes the same small interface:

    UNITS                          -> mapping/collection of supported unit symbols
    convert(value, from_unit, to_unit) -> float
"""

from importlib import import_module

CATEGORIES = ("length", "temperature", "weight")


def get_converter(category):
    """Return the converter module for a category name (case-insensitive)."""
    if not isinstance(category, str):
        raise TypeError("category must be a string")
    key = category.strip().lower()
    if key not in CATEGORIES:
        raise ValueError(
            f"Unknown category '{category}'. Choose from: {', '.join(CATEGORIES)}"
        )
    return import_module(f"converters.{key}")
