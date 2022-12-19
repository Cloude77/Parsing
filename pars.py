import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text




def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('main', id='content').find('article').find('h1').text
    return h1


def main():
    url = 'https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Introduction'
    print(get_data(get_html(url)))



if __name__ == '__main__':
    main()