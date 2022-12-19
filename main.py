import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text




def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', class_='wp-site-blocks').find('header').find('h1', class_='wp-block-wporg-random-heading has-heading-cta-font-size')
    h2 = soup.find('h1', class_='wp-block-wporg-random-heading has-heading-cta-font-size').text
    return h1, h2



def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))



if __name__ == '__main__':
    main()

