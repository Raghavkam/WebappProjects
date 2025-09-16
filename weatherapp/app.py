from flask import Flask, request, render_template, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flash messages

@app.route('/')
def index():
    return redirect(url_for('weather_form'))

@app.route('/getweather', methods=['GET', 'POST'])
def weather_form():
    if request.method == 'POST':
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        if not latitude or not longitude:
            flash('Latitude and Longitude are required!')
            return redirect(url_for('weather_form'))

        try:
            lat = float(latitude)
            lon = float(longitude)
        except ValueError:
            flash('Invalid latitude or longitude!')
            return redirect(url_for('weather_form'))

        return redirect(url_for('weather_results', latitude=lat, longitude=lon))
    return render_template('form.html')

@app.route('/getweather/results', methods=['GET'])
def weather_results():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    if not latitude or not longitude:
        return redirect(url_for('weather_form'))

    try:
        lat = float(latitude)
        lon = float(longitude)
    except ValueError:
        flash('Invalid latitude or longitude!')
        return redirect(url_for('weather_form'))

    # Validate the input to ensure it's within the US boundaries
    if not (24 <= lat <= 49 and -125 <= lon <= -66):
        flash('Coordinates are outside the US boundaries!')
        return redirect(url_for('weather_form'))

    weather_api_url = f"https://api.weather.gov/points/{lat},{lon}"
    try:
        response = requests.get(weather_api_url)
        response.raise_for_status()
        forecast_url = response.json()['properties']['forecast']
        forecast_response = requests.get(forecast_url)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()
        periods = forecast_data['properties']['periods']
    except requests.exceptions.RequestException as e:
        flash(f'Error fetching weather data: {e}')
        return redirect(url_for('weather_form'))

    return render_template('results.html', periods=periods, latitude=lat, longitude=lon)

if __name__ == '__main__':
    app.run(debug=True)
