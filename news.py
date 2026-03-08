import requests
import os
from dotenv import load_dotenv

# This loads the API key from the .env fi;e
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# This uses a newsapi.org API key, and gets news data. You need an account for this to work, along with putting in your key in the .env file


def news_getter(topic, headline_amount):
    try:
        if topic == "":
            # This gets the data from newsapi.org using the request function
            response_news = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}")
        else:
            # This is the almost the same as the one above, but it also adds a topic, so we can filter by topic
            response_news = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=us&category={topic}&apiKey={NEWS_API_KEY}"
            )
    # This block is for if the user has no internet connection
    except requests.exceptions.ConnectionError:
        print("No internet connection")
        return
    data_news = response_news.json()
    # This block checks if there are articles, if not, it breaks
    if "articles" not in data_news:
        print("Bad API key")
        return
    else:
        article = data_news['articles']
        articles_to_show = article if headline_amount is None else article[:headline_amount]
        # This enumerate function adds numbers to the begining of the news. It also prints only a certain amount of headline the user wants
        for index, item in enumerate(articles_to_show, 1):
            print(f"{index}. {item['title']}")
