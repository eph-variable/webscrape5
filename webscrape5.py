import requests
from bs4 import BeautifulSoup
import re

def scrape(url):
	print(f"SCRAPED FROM: {url}\n")
	page = requests.get(url)
	page_html = BeautifulSoup(page.content, 'lxml')
	print(page_html.prettify())


# scrape("https://stackoverflow.com/questions/36971604/getting-wrong-page-source-when-calling-url-from-python")

if __name__ == "__main__":
	scrape("https://stackoverflow.com/questions/36971604/getting-wrong-page-source-when-calling-url-from-python")
