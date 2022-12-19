import requests
from bs4 import BeautifulSoup
import csv
import re


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)




def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['url'], data['price']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_='sc-f7a61dda-3 kCSmOD cmc-table').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')

        try:
            name = tds[2].find('p', class_='sc-e225a64a-0 ePTNty').text.strip()
        except:
            name = ''
        print(name)

        try:
            url = 'https://coinmarketcap.com/' + tds[2].find('a').get('href')
        except:
            url = ''

        try:
            price = tds[3].find('span')
        except:
            price = ''

        data = {'name': name,
                'url': url,
                'price': price}

        write_csv(data)


def main():
    url = 'https://coinmarketcap.com/'
    # get_page_data(get_html(url))
    while True:
        get_page_data(get_html(url))

        soup = BeautifulSoup(get_html(url), 'lxml')

        try:
            pattern = 'page'
            url = 'https://coinmarketcap.com/' + soup.find('ul', class_='pagination').find('a', text=re.compile(pattern)).get('href')
        except:
            break


if __name__ == '__main__':
    main()
