# db.py
import os
import sqlite3

from flask import jsonify

db_path = '/data/booking-database.db'
createfile = './setup/createfile.sql'

def initialize_database():
    if not os.path.exists(db_path):
        print(f"Database {db_path} bestaat niet, wordt aangemaakt...")

        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        with open(createfile, 'r') as file:
            sql_script = file.read()

        cursor.executescript(sql_script)

        connection.commit()
        connection.close()
    else:
        print(f"Database {db_path} bestaat al. Geen actie nodig.")

def add_booking(event):
    try:
        if not event:
            return jsonify({"error": "Event is required"}), 400

        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO booking (event) VALUES (?)", (event,))

        connection.commit()

        booking_id = cursor.lastrowid

        connection.close()

        return jsonify({"message": "Booking created", "bookingId": booking_id}), 201

    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}"}), 500


def get_bookings_db():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM booking")
    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]

    bookings = []
    for row in rows:
        booking = dict(zip(columns, row))
        bookings.append(booking)

    connection.close()
    return bookings
