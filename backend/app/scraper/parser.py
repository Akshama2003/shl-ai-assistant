from bs4 import BeautifulSoup


def parse_assessments(html: str):

    soup = BeautifulSoup(html, "lxml")

    assessments = []

    cards = soup.find_all("article")

    for card in cards:

        title = ""

        url = ""

        description = ""

        category = ""

        link = card.find("a")

        if link:
            title = link.get_text(" ", strip=True)

            href = link.get("href", "")

            if href.startswith("/"):
                href = "https://www.shl.com" + href

            url = href

        p = card.find("p")

        if p:
            description = p.get_text(" ", strip=True)

        assessments.append(
            {
                "name": title,
                "url": url,
                "description": description,
                "category": category,
                "test_type": ""
            }
        )

    return assessments