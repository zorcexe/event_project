"""
Erstellt eine SQLite-Datenbank mit den Tabellen:

- company
- sales

Beziehung:
company (1) -> sales (N)

Aufruf:
    uv run create_sample_db.py
"""

import sqlite3
from pathlib import Path
import random
from datetime import datetime, timedelta


DB_PATH = Path(__file__).resolve().parent / "external_data_neu.sqlite3"


def generate_sales(num_sales: int = 200):
    products = [
        ("Laptop", 1200.0),
        ("Monitor", 300.0),
        ("Keyboard", 50.0),
        ("Mouse", 25.0),
        ("Docking Station", 180.0),
        ("Webcam", 75.0),
    ]

    start_date = datetime(2026, 1, 1)

    sales = []
    for _ in range(num_sales):
        company_id = random.randint(1, 3)

        product_name, base_price = random.choice(products)

        quantity = random.randint(1, 20)

        # leichte Preisvariation
        price = round(base_price * random.uniform(0.8, 1.2), 2)

        sold_at = start_date + timedelta(days=random.randint(0, 60))
        sold_at_str = sold_at.strftime("%Y-%m-%d")

        sales.append((company_id, product_name, quantity, price, sold_at_str))

    return sales


def create_database() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE company (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price_per_unit REAL NOT NULL,
            sold_at TEXT NOT NULL,
            FOREIGN KEY (company_id) REFERENCES company(id)
        );
    """
    )

    companies = [
        ("SolarSoft GmbH", "Berlin"),
        ("DataFoods AG", "Hamburg"),
        ("Pixel & Co", "München"),
    ]

    cursor.executemany(
        """
        INSERT INTO company (name, city)
        VALUES (?, ?);
    """,
        companies,
    )

    sales = generate_sales(200)

    cursor.executemany(
        """
        INSERT INTO sales (company_id, product_name, quantity, price_per_unit, sold_at)
        VALUES (?, ?, ?, ?, ?);
    """,
        sales,
    )

    conn.commit()
    conn.close()

    print(f"Datenbank erstellt: {DB_PATH.resolve()}")


if __name__ == "__main__":
    create_database()
