import json

from app.scraper.crawler import fetch
from app.scraper.parser import parse_product_cards


URL = "https://www.shl.com/products/"


html = fetch(URL)

cards = parse_product_cards(html)

with open(
    "data/catalog.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        cards,
        f,
        indent=4
    )

print(len(cards))