from django.shortcuts import render
import requests
import datetime
import json  # Import JSON for debugging

def index(request):
    # Fix: Use raw string (r"") to prevent backslash errors in file path
    api_key = open(r"C:\weather app\API_key", "r").read().strip()
    
    # Fix: Use 'forecast' API instead of 'onecall' for free-tier users
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}'

    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, api_key, current_weather_url, forecast_url)

        if city2:
            weather_data2, daily_forecasts2 = fetch_weather_and_forecast(city2, api_key, current_weather_url, forecast_url)
        else:
            weather_data2, daily_forecasts2 = None, None

        context = {
            'weather_data1': weather_data1,
            'daily_forecasts1': daily_forecasts1,
            'weather_data2': weather_data2,
            'daily_forecasts2': daily_forecasts2,
        }

        return render(request, 'weather_app/index.html', context)
    else:
        return render(request, 'weather_app/index.html')


def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    # Fetch current weather data
    response = requests.get(current_weather_url.format(city, api_key)).json()
    print("Current Weather API Response:", json.dumps(response, indent=4))  # Debugging

    # Fix: Handle API errors gracefully
    if "coord" not in response:
        print(f"Error: Could not fetch coordinates for {city}. API Response:", json.dumps(response, indent=4))
        return None, None

    lat, lon = response['coord']['lat'], response['coord']['lon']

    # Fetch forecast data
    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()
    print("Forecast API Response:", json.dumps(forecast_response, indent=4))  # Debugging

    # Fix: Check if 'list' (forecast data) exists in API response
    if "list" not in forecast_response:
        print(f"Error: 'list' data missing in forecast API response for {city}.")
        return None, None  # Avoid crashing by returning None

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    daily_forecasts = []
    for forecast in forecast_response['list'][:5]:  # Use 'list' instead of 'daily'
        daily_forecasts.append({
            'day': datetime.datetime.fromtimestamp(forecast['dt']).strftime('%A'),
            'min_temp': round(forecast['main']['temp_min'] - 273.15, 2),
            'max_temp': round(forecast['main']['temp_max'] - 273.15, 2),
            'description': forecast['weather'][0]['description'],
            'icon': forecast['weather'][0]['icon'],
        })

    return weather_data, daily_forecasts
