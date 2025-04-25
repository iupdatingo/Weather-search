from flask import Flask, jsonify, render_template, request
import datetime as dt
import requests
from urllib.parse import quote
import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv('OPENWEATHER_API_KEY')
if not API_KEY:
    raise Exception("OPENWEATHER_API_KEY environment variable not found. Please check your .env file.")

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return round(celsius, 2), round(fahrenheit, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    try:
        city = request.args.get('city')
        if not city:
            return jsonify({"error": "City parameter is required"}), 400

        # URL encode the city parameter
        encoded_city = quote(city)
        url = f"{BASE_URL}appid={API_KEY}&q={encoded_city}"

        try:
            # Make the API request with timeout
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
        except requests.RequestException as e:
            logging.error(f"API request failed: {str(e)}")
            return jsonify({"error": "Failed to fetch weather data"}), 503

        if data.get('cod') != 200:
            error_msg = data.get('message', 'Failed to retrieve weather data')
            logging.error(f"API error: {error_msg}")
            return jsonify({"error": error_msg}), 400

        try:
            # Parse weather data
            temperature_kelvin = data['main']['temp']
            temperature_celsius, temperature_fahrenheit = kelvin_to_celsius_fahrenheit(temperature_kelvin)
            feels_like_kelvin = data['main']['feels_like']
            feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

            weather_data = {
                "temperature_celsius": temperature_celsius,
                "temperature_fahrenheit": temperature_fahrenheit,
                "feels_like_celsius": feels_like_celsius,
                "feels_like_fahrenheit": feels_like_fahrenheit,
                "humidity": data['main']['humidity'],
                "description": data['weather'][0]['description'],
                "wind_speed": data['wind']['speed'],
                "sunrise": dt.datetime.fromtimestamp(
                    data['sys']['sunrise'] + data.get('timezone', 0),
                    dt.timezone.utc
                ).strftime('%Y-%m-%d %H:%M:%S'),
                "sunset": dt.datetime.fromtimestamp(
                    data['sys']['sunset'] + data.get('timezone', 0),
                    dt.timezone.utc
                ).strftime('%Y-%m-%d %H:%M:%S')
            }
            return jsonify(weather_data)

        except (KeyError, TypeError) as e:
            logging.error(f"Failed to parse weather data: {str(e)}")
            return jsonify({"error": "Invalid data received from weather service"}), 500

    except Exception as e:
        logging.error(f"Unexpected error in weather route: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
