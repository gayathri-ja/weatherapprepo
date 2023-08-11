def syntax_test(code_str):
    try:
        compile(code_str, '<string>', 'exec')
        print("Syntax is valid.")
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Your app.py script
app_code = """
import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = '83196fbc57763187a3cab13e3bcd1e59'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
app = Flask(__name__, static_url_path='/static')

def get_weather_data(city_name):
    try:
        params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

@app.route('/', methods=['GET', 'POST'])
def weather_app():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)

        if not weather_data:
            error_message = "City not found or API request failed. Please try again."

    return render_template('weather.html', weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
"""

# Call the syntax_test function with the app.py code
syntax_test(app_code)
