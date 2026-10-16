import os
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parent / ".env")

API_KEY = os.environ.get("API_KEY") or os.environ.get("API_NINJAS_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"
REQUEST_TIMEOUT = 15


def fetch_data(animal_name):
    """Fetch matching animals as a list of dictionaries.

    Each animal may contain name, taxonomy, locations and characteristics.
    Return an empty list when no animals match.
    Raise ValueError if the key is missing or fetching valid data fails.
    """
    if not API_KEY or not API_KEY.strip():
        raise ValueError("Bitte API_KEY in der .env-Datei einrichten.")

    try:
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY},
            params={"name": animal_name},
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        animals = response.json()
    except (requests.RequestException, ValueError) as error:
        raise ValueError("Tierdaten konnten nicht abgerufen werden.") from error

    if not isinstance(animals, list) or not all(
        isinstance(animal, dict) for animal in animals
    ):
        raise ValueError("Die API hat keine gültige Tierliste zurückgegeben.")
    return animals
