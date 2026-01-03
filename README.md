# Py_remembered.py

A notebook-style Python refresher that demonstrates **core Python data types**, **functions**, **OOP concepts**, and a practical mini-toolkit for **NumPy**, **Pandas**, **file I/O (CSV/Excel)**, **SQL Server connectivity**, **REST API calls**, and **basic web scraping**. :contentReference[oaicite:1]{index=1}

## What’s inside

The file is organized into IDE “cells” using `#%%` blocks (common in Spyder / VS Code). Sections include:

- **Data types**
  - List operations (`append`, `insert`, update by index, `pop`, slicing)
  - Tuple basics (`count`, `len`)
  - Set behavior (uniqueness, `difference`, `intersection`)
  - Dictionary basics (`get`, adding/updating keys)
- **Functions**
  - Default parameters, multiple parameters, returning values (e.g., net salary calculation)
- **Object-Oriented Programming (OOP)**
  - Class vs instance attributes (and why class attributes can be shared unexpectedly)
  - `__init__`, methods, simple state changes
  - OOP principles: **Encapsulation**, **Inheritance**, **Polymorphism**, **Abstraction**
- **NumPy**
  - Arrays, reshape/ravel, basic stats, vectorized arithmetic, stacking, copies
- **Pandas**
  - Series/DataFrame basics, `head/tail/sample`, `loc` updates/inserts, `drop`
  - `merge` (inner/left/right) and `concat` (SQL UNION-like behavior)
- **Dataset loading & export**
  - `read_csv` with selected columns and row limit
  - `read_excel`, missing value handling, derived columns, filtering, `to_excel`
- **SQL Server (connection string skeleton)**
  - SQLAlchemy + pyodbc connection string example
- **API calls**
  - `requests.get` + JSON → DataFrame → Excel
  - `requests.post` example
- **Web scraping**
  - `BeautifulSoup` basics + pagination example
  - Custom `User-Agent` header example
  - Includes `time.sleep(10)` delays

## Requirements

- Python **3.9+** recommended
- Packages used in the script:

  - `numpy`
  - `pandas`
  - `requests`
  - `beautifulsoup4`
  - `sqlalchemy`
  - `pyodbc` (only needed for SQL Server section)
  - `openpyxl` (recommended for Excel read/write via Pandas)

Install commonly needed packages:

```bash
pip install numpy pandas requests beautifulsoup4 sqlalchemy pyodbc openpyxl
