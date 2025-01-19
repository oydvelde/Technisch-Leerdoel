from flask import Flask, jsonify, request
from flask_cors import CORS
from db import initialize_database, add_booking, get_bookings_db
import requests

app = Flask(__name__)
CORS(app)

with app.app_context():
    initialize_database()

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"message": "Backend server draait!"})

@app.route('/events', methods=['GET'])
def get_events():
    response = requests.get("http://event-service-springboot:5050/events")

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Fout bij het ophalen van gegevens van de andere API"}), 500

@app.route('/booking', methods=['POST'])
def create_booking():
    return add_booking(request.get_json().get('event'))

@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(get_bookings_db())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6060, debug=True)