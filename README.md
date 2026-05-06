# resta

A command-line tool that loads restaurant menus from a remote JSON source
and displays them grouped by company.

## Project structure

```
resta/
├── app.py                    # Entry point
└── Modelos/
    ├── Re.py                 # Restaurante class
    ├── eval.py               # Eval class
    └── Menus/
        ├── it_me.py          # ItMe abstract base class
        ├── plate.py          # Plate (food items)
        └── bev.py            # Bev (beverages)
```

## Requirements

- Python 3.10+
- [requests](https://pypi.org/project/requests/)

```bash
pip install requests
```

## Usage

Run from the `resta/` directory:

```bash
python app.py
```

You will be prompted for a URL:

```
Source URL: https://example.com/menu.json
```

## JSON format

The URL must return a JSON array where each object represents one menu item:

```json
[
  {
    "Company": "Plaza mais",
    "Item": "Pãozinho",
    "price": 3.0,
    "description": "Pão delicia baiano (Alérgicos: contém derivados de leite)"
  },
  {
    "Company": "Plaza mais",
    "Item": "Suco de Melancia",
    "price": 6.0,
    "size": 500
  }
]
```

| Field         | Type   | Required for       |
|---------------|--------|--------------------|
| `Company`     | string | all items          |
| `Item`        | string | all items          |
| `price`       | number | all items          |
| `description` | string | plates (`Plate`)   |
| `size`        | number | beverages (`Bev`)  |

Items with a `description` key are created as `Plate` (10 % discount applied).  
Items with a `size` key are created as `Bev` (8 % discount applied).

## Class overview

| Class         | File                      | Responsibility                               |
|---------------|---------------------------|----------------------------------------------|
| `Restaurante` | `Modelos/Re.py`           | Holds menu items and evaluations             |
| `Eval`        | `Modelos/eval.py`         | Stores a single client score (0–5)           |
| `ItMe`        | `Modelos/Menus/it_me.py`  | Abstract base; provides `from_dict` factory  |
| `Plate`       | `Modelos/Menus/plate.py`  | Food plate with description                  |
| `Bev`         | `Modelos/Menus/bev.py`    | Beverage with volume (ml)                    |
