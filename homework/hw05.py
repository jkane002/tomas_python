
import requests
from bs4 import BeautifulSoup


url = input("Enter a website to extract the URL's from: ")

response = requests.get(url)
page = response.content
soup =  BeautifulSoup(page, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
