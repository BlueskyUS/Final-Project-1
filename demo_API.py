import requests

API_KEY = "  asfefafa  "
API_BASE_URL = "https://api.mytimes.com/svc/search/v2/articlesesarch.json"

def search_articles(search_term):
    params = {
        "q": search_term,
        "api_key":API_KEY
    }
    response = requests.get(API_BASE_URL,params)
    return response.json()

def display_results(search_results):
    docs = search_results["response"]["docs"]
    for doc in docs:
        article_web_url = doc["web_url"]
        article_headline = doc["headline"]["main"]

        print(article_headline + "(" + article_web_url + ")")

    while True:
        search_term = input("Your search term: ")
        search_results = search_articles(search_term)
        display_results(search_results)
        print("")