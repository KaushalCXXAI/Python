import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = "https://books.toscrape.com/"

# Send request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract book titles and prices
books = soup.find_all("article", class_="product_pod")

data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    data.append({"Title": title, "Price": price})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("books1.csv", index=True)

print("Scraping complete! Data saved to books.csv")