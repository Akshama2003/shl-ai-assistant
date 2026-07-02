import json

from app.scraper.crawler import fetch_page

URL = "https://www.shl.com/solutions/products/product-catalog/"

print("Downloading catalog...")

html = fetch_page(URL)

with open("catalog_page.html", "w", encoding="utf8") as f:
    f.write(html)

print("Saved HTML to catalog_page.html")