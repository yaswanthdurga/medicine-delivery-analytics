import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "database" / "delivery.db"


def load_data():
    connection = sqlite3.connect(DATABASE_FILE)

    query = """
    SELECT *
    FROM medicine_orders
    """

    df = pd.read_sql_query(query, connection)

    connection.close()

    return df


def generate_summary():

    df = load_data()

    total_orders = len(df)

    delivered_orders = len(
        df[df["delivery_status"] == "Delivered"]
    )

    delayed_orders = len(
        df[df["delivery_status"] == "Delayed"]
    )

    cancelled_orders = len(
        df[df["delivery_status"] == "Cancelled"]
    )

    delivery_success_rate = (
        delivered_orders / total_orders * 100
    )

    average_delivery_time = df[
        df["delivery_status"] != "Cancelled"
    ]["delivery_time_hours"].mean()

    total_revenue = df[
        df["delivery_status"] != "Cancelled"
    ]["order_value"].sum()

    print("\n===== MEDICINE DELIVERY ANALYTICS =====")

    print(f"Total Orders: {total_orders}")

    print(f"Delivered Orders: {delivered_orders}")

    print(f"Delayed Orders: {delayed_orders}")

    print(f"Cancelled Orders: {cancelled_orders}")

    print(
        f"Delivery Success Rate: "
        f"{delivery_success_rate:.2f}%"
    )

    print(
        f"Average Delivery Time: "
        f"{average_delivery_time:.2f} hours"
    )

    print(
        f"Total Revenue: "
        f"₹{total_revenue:,.2f}"
    )


if __name__ == "__main__":
    generate_summary()