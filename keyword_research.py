import requests

def get_keywords_from_google(query, max_keywords=4):
    url = "http://suggestqueries.google.com/complete/search"
    params = {
        "client": "firefox",
        "q": query
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)
    suggestions = response.json()[1]

    return suggestions[:max_keywords]

# Example usage
if __name__ == "__main__":
    product_title = "Wireless Bluetooth Headphones"
    keywords = get_keywords_from_google(product_title)
    print(f"Keywords for '{product_title}': {keywords}")
