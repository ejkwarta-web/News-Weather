from weather import get_coordinates, get_weather
from news import news_getter
import requests
import os
from dotenv import load_dotenv
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# This is the main function for the code, it calls the other functions and prints the data. It also takes in values for the functions.


def main():
    while True:
        city = input("What city are you in? >>>")
        if city == "debug":
            debug_mode()
            continue
        topic = input(
            "What topic of news would you like? Or do nothing for all >>>")
        # This input is used for seeing how many headlines the user wants
        headline_input = input(
            "Enter the amount of headlines you want, or nothing for all >>>")
        if headline_input == "":
            headline_amount = None
        else:
            headline_amount = int(headline_input)
        result = get_coordinates(city)
        if result is None:
            continue
        # This prints all the data
        else:
            latitude, longitude, city = result
            temp, sky_to_print = get_weather(latitude, longitude)
            print("---Weather---")
            print(f"The temperature in {city} is {temp}°F.")
            print(f"The weather type is {sky_to_print.lower()}.")
            print("---News---")
            news_getter(topic, headline_amount)

# This is a debug mode for testing, you can access it by doing debug in the "what city are you in" querry


def debug_mode():
    try:
        response_weather = requests.get(
            "https://api.open-meteo.com/v1/forecast?latitude=38.63&longitude=-90.20&current=temperature_2m")
        data_weather = response_weather.json()
        response_news = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}")
        data_news = response_news.json()
    except requests.exceptions.ConnectionError:
        print("No internet connection")
        return
    print("---Debug Mode ---")
    print("1. Run diagnostics")
    print("2. Show raw API data")
    choice = input(">>>")
    if choice == "1":
        if NEWS_API_KEY is not None:
            print("API Key: Loaded")
        else:
            print("API Key: Missing")
        if "current" in data_weather:
            print("Weather API: Working")
        else:
            print("Weather API: Failed")
        if "articles" in data_news:
            print("News API: Working")
        else:
            print("News API: Failed")
    elif choice == "2":
        print("---Weather Data---")
        print(data_weather)
        print("---News Data---")
        print(data_news)


main()
