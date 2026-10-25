"""Command-line unit converter.

Examples:
    python app.py length 5 km mi
    python app.py temperature 100 c f
    python app.py weight 2.5 kg lb
    python app.py --list
"""

import argparse
import sys

from converters import CATEGORIES, get_converter


def format_result(value, from_unit, to_unit, result):
    """Return a human-readable line such as '5 km = 3.1069 mi'."""
    number = f"{result:.4f}".rstrip("0").rstrip(".")
    if number in ("", "-0"):
        number = "0"
    return f"{value:g} {from_unit} = {number} {to_unit}"


def list_units():
    lines = []
    for category in CATEGORIES:
        try:
            module = get_converter(category)
        except ModuleNotFoundError:
            continue  # feature not merged yet
        lines.append(f"{category}: {', '.join(module.UNITS)}")
    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(description="Simple unit converter")
    parser.add_argument("category", nargs="?", help="length, temperature or weight")
    parser.add_argument("value", nargs="?", type=float, help="number to convert")
    parser.add_argument("from_unit", nargs="?", help="unit to convert from")
    parser.add_argument("to_unit", nargs="?", help="unit to convert to")
    parser.add_argument("--list", action="store_true", help="list supported units")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list:
        print(list_units())
        return 0

    if None in (args.category, args.value, args.from_unit, args.to_unit):
        parser.print_usage(sys.stderr)
        return 2

    try:
        converter = get_converter(args.category)
        result = converter.convert(args.value, args.from_unit, args.to_unit)
    except (ValueError, TypeError, ModuleNotFoundError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(format_result(args.value, args.from_unit, args.to_unit, result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
