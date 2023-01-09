import requests
from bs4 import BeautifulSoup

def run():
    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

    r = requests.get(url)
    r_html = r.text
    
    soup = BeautifulSoup(r_html,'html.parser')

    for i in soup.find_all("p"):
        print(i.get_text())

if __name__ == '__main__':
    run()