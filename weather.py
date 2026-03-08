import requests
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Freezing fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Heavy drizzle",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Light showers",
    81: "Moderate showers",
    82: "Heavy showers",
    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Heavy thunderstorm with hail"
}

# This function gets the coordinates from a city name


def get_coordinates(city):
    try:
        response_coordinates = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1")
    except requests.exceptions.ConnectionError:
        print("No internet connection")
        return
    data_coordinates = response_coordinates.json()
    if "results" not in data_coordinates:
        print("Error: city not found")
        return
    else:
        results_coordinates = data_coordinates["results"]
        longitude = results_coordinates[0]["longitude"]
        latitude = results_coordinates[0]["latitude"]
        return latitude, longitude, city

# This function uses the coordinates and gets weather data


def get_weather(latitude, longitude):
    try:
        response_weather = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weathercode&temperature_unit=fahrenheit")
    except requests.exceptions.ConnectionError:
        print("No internet connection")
        return
    data_weather = response_weather.json()
    results_weather = data_weather["current"]
    temp = results_weather["temperature_2m"]
    sky_type = results_weather["weathercode"]
    sky_to_print = WEATHER_CODES[sky_type]
    return temp, sky_to_print
