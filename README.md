# Unit Converter

A small command-line unit converter written in Python, with a pytest test suite,
GitHub Actions CI, and a GitHub Pages project page.

Project status: Development in progress.

**Live project page:** https://mehdibuilds.github.io/unit-converter/

## Team

**Theme:** Unit Converter

| Member | GitHub username | Feature | Branch |
| --- | --- | --- | --- |
| El Mehdi Rahmoune | @mehdibuilds | Feature A: length conversion (`converters/length.py`) | `feature/length` |
| Hanae Cherkaoui | @HanaeCherk90 | Feature B: temperature conversion (`converters/temperature.py`) | `feature/temperature` |
| Hiba El Adraoui | @HibaEladraoui | Feature C: weight conversion (`converters/weight.py`) | `feature/weight` |

## Features

- **Length** – mm, cm, m, km, in, ft, yd, mi
- **Temperature** – Celsius, Fahrenheit, Kelvin (rejects values below absolute zero)
- **Weight** – mg, g, kg, t, oz, lb, st (rejects negative weights)

All converters validate their input and raise `TypeError` for non-numeric values
and `ValueError` for unknown units or invalid values.

## Run it

Requires Python 3.10 or newer.

```bash
python app.py length 5 km mi          # 5 km = 3.1069 mi
python app.py temperature 100 c f     # 100 c = 212 f
python app.py weight 2.5 kg lb        # 2.5 kg = 5.5116 lb
python app.py --list                  # show every supported unit
```

## Run the tests

```bash
pip install -r requirements.txt
pytest
```

## Project layout

```
app.py                 command-line interface
converters/            one module per feature (length, temperature, weight)
tests/                 pytest tests, one file per feature
docs/                  GitHub Pages project page
.github/workflows/     CI workflow (runs pytest on every push and pull request)
```

## Workflow

`main` is protected: changes arrive through feature branches and pull requests,
each needing one approval and a passing `pytest` check.
