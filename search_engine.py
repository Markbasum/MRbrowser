import requests
from bs4 import BeautifulSoup

class GoogleSearchEngine:
    
    def __init__(self, show_search_results):
        self.show_search_results = show_search_results

    def search(self, query):
        search_results = self.get_search_results(query)
        self.show_search_results(search_results)

    def get_search_results(self, query):
        url = f"https://www.google.com/search?q={query}&num=10"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = []
        for result in soup.find_all('div', {'class': 'g'}):
            link = result.find('a').get('href')[7:]
            title = result.find('h3').text
            description = result.find('span', {'class': 'aCOpRe'}).text
            search_results.append({
                'link': link,
                'title': title,
                'description': description
            })
        return search_results

    def open_url(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
