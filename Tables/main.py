import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    r = requests.get(url)
    return r.text



def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['symbol'],
                         data['url'],
                         data['price']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table').find('tbody').find_all('tr')



    for tr in trs:
        tds = tr.find_all('td')  # return list of object
        name = tds[2].find('p', class_='sc-e225a64a-0 ePTNty').text
        symbol = tds[2].find('p', class_='sc-e225a64a-0 dfeAJi coin-item-symbol').text
        url = 'https://coinmarketcap.com/' + tds[2].find('a').get('href')
        price = tds[3].find('span')

        data = {'name': name,
                'symbol': symbol,
                'url': url,
                'price': price}

        write_csv(data)


def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
