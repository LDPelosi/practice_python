import requests
from bs4 import BeautifulSoup

def run():
    url = 'https://www.nytimes.com/'

    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html,'html.parser')


    for i in soup.find_all("h3"):
        print(i.get_text())


if __name__ == '__main__':
    run()