from bs4 import BeautifulSoup
import requests


class UnsplashCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

    def get_soup(self, query: str) -> BeautifulSoup:
        query = query.replace(' ', '-')
        url = f'https://unsplash.com/s/photos/{query}'
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def parse_soup(self, soup: BeautifulSoup) -> list:
        divs = soup.find_all('figure', {'data-test': 'photo-grid-multi-col-figure'})
        images = {}
        for div in divs:
            images[div.find('img')['src']] = div.find('a')['href']
        return images


if __name__ == '__main__':
    freepik = UnsplashCrawler()
    query = input('Search something: ')
    soup = freepik.get_soup(query)
    images = freepik.parse_soup(soup)
    for image, hyperlink in images.items():
        print(image, hyperlink)