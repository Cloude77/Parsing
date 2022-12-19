import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text

def refind(s):
    # 1,980 total ratings
    r = s.split(' ')[0] # 1,980
    return r.replace(',', '')

def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))



def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article') # all tags article.List


    for plugin in plugins:
        # [plagin1, plugin2, plugin3, plugin4]
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')

        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refind(r)
        print(rating)

        data = {'name': name,
                'url': url,
                'reviews': rating }

        write_csv(data)



def main():
   url = 'https://wordpress.org/plugins/'
   get_data(get_html(url))

if __name__ == '__main__':
    main()

