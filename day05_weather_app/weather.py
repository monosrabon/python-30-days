# Handles fetching weather data from OpenWeather API.

import urllib.request  # To make HTTP requests without 'requests'
from config import API_KEY, BASE_URL  # Import API settings


def get_weather(city_name: str) -> dict:
    """
    Fetch weather data for a given city using OpenWeather API.

    Parameters:
        city_name (str): Name of the city (e.g., "Dhaka").

    Returns:
        dict: Weather information or error message.
    """

    # Parameters we will send with the API request
    params = {
        "q": city_name,     # city name
        "appid": API_KEY,   # API key
        "units": "metric",  # temperature in Celsius
        "lang": "en"        # response language in English
    }

    import urllib.parse
    import json
    try:
        # Build the full URL with query parameters
        url = BASE_URL + "?" + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                return {"error": f"HTTP Error: {response.status}"}
            data = json.loads(response.read().decode())

        # Extract useful info from API response
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"].capitalize()
        }
        return weather_info
    except urllib.error.HTTPError as http_err:
        return {"error": f"HTTP Error: {http_err.code} {http_err.reason}"}
    except urllib.error.URLError as url_err:
        return {"error": f"Request Error: {url_err.reason}"}
    except KeyError:
        return {"error": "Invalid city name or data unavailable"}
