
import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.text vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    # stazeni obsahu stranky
    response = requests.get(url)

    # kontrola navratoveho kodu
    if response.status_code != 200:
        raise Exception(f"Chyba pri nacitani URL {url}: HTTP {response.status_code}")

    html = response.text

    # najdeme vsechny href z <a ... href="...">
    hrefs = re.findall(r'<a\s+[^>]*href="([^"]+)"', html)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]  # prvni argument z prikazove radky
        hrefs = download_url_and_get_all_hrefs(url)

        # vypiseme vsechny nalezene odkazy po radcich
        for h in hrefs:
            print(h)

    except IndexError:
        print("Pouziti: python sixth.py <url>")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")

