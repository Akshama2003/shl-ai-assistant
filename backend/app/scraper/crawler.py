import requests

BASE_URL = "https://www.shl.com"


def fetch(url: str):

    response = requests.get(
        url,
        timeout=30,
        headers={
            "User-Agent":
            "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    return response.text