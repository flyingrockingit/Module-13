import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('WEATHER_API')


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')

        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
            else:
                error = "City not found, please try again!"
        else:
            error = "Please enter a city name."

    return render_template('index.html', weather=weather_data, error=error)


if __name__ == '__main__':
    app.run(debug=True)