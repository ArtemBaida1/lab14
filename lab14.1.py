import requests
from bs4 import BeautifulSoup

def parse_google_scholar(profile_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    response = requests.get(profile_url, headers=headers)
    if response.status_code != 200:
        print("Не вдалося отримати доступ до профілю.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for link in soup.find_all('a', class_='gsc_a_at'):
        href = link.get('href')
        if href:
            full_url = f"https://scholar.google.com{href}"
            links.append(full_url)

    with open('links.txt', 'w') as file:
        for link in links:
            file.write(link + '\n')

    print(f"Знайдено {len(links)} посилань, збережено в links.txt")

profile_url = "https://scholar.google.com/citations?user=xbhZFHYAAAAJ"
parse_google_scholar(profile_url)
