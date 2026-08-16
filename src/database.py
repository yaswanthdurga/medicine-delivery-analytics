import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "medicines.csv"
DATABASE_FILE = BASE_DIR / "database" / "delivery.db"


def create_database():
    DATABASE_FILE.parent.mkdir(exist_ok=True)

    df = pd.read_csv(DATA_FILE)

    connection = sqlite3.connect(DATABASE_FILE)

    df.to_sql(
        "medicine_orders",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print("Database created successfully.")
    print(f"Database location: {DATABASE_FILE}")


if __name__ == "__main__":
    create_database()