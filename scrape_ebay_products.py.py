import requests
from bs4 import BeautifulSoup

def scrape_ebay_products(search_term="electronics", max_results=5):
    url = f"https://www.ebay.com/sch/i.html?_nkw={search_term}&_sop=12"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    listings = soup.select(".s-item")[:max_results]

    for item in listings:
        title = item.select_one(".s-item__title")
        link = item.select_one(".s-item__link")
        price = item.select_one(".s-item__price")

        if title and link and price:
            product_info = {
                "title": title.text.strip(),
                "link": link["href"],
                "price": price.text.strip()
            }
            products.append(product_info)

    return products

# Example usage:
if __name__ == "__main__":
    results = scrape_ebay_products("headphones", max_results=3)
    for product in results:
        print(product)
