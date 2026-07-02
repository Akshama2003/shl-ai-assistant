from bs4 import BeautifulSoup


def parse_product_cards(html):

    soup = BeautifulSoup(html, "lxml")

    cards = []

    for card in soup.find_all("a"):

        href = card.get("href")

        title = card.get_text(strip=True)

        if href and title:

            cards.append(
                {
                    "title": title,
                    "url": href
                }
            )

    return cards