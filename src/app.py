from flask import Flask, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "database" / "delivery.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return jsonify({
        "project": "Medicine Delivery & Tracking Analytics System",
        "status": "running"
    })


@app.route("/api/orders")
def get_orders():

    connection = get_connection()

    orders = connection.execute(
        "SELECT * FROM medicine_orders"
    ).fetchall()

    connection.close()

    return jsonify([
        dict(order)
        for order in orders
    ])


@app.route("/api/summary")
def get_summary():

    connection = get_connection()

    total_orders = connection.execute(
        "SELECT COUNT(*) FROM medicine_orders"
    ).fetchone()[0]

    delivered = connection.execute(
        """
        SELECT COUNT(*)
        FROM medicine_orders
        WHERE delivery_status = 'Delivered'
        """
    ).fetchone()[0]

    delayed = connection.execute(
        """
        SELECT COUNT(*)
        FROM medicine_orders
        WHERE delivery_status = 'Delayed'
        """
    ).fetchone()[0]

    cancelled = connection.execute(
        """
        SELECT COUNT(*)
        FROM medicine_orders
        WHERE delivery_status = 'Cancelled'
        """
    ).fetchone()[0]

    connection.close()

    return jsonify({
        "total_orders": total_orders,
        "delivered": delivered,
        "delayed": delayed,
        "cancelled": cancelled
    })


if __name__ == "__main__":
    app.run(debug=True)