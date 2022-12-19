import requests
from bs4 import  BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    if r.ok: # 200  ## 403 404
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('yaca.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['text'],
                         data['year']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    arts = soup.find_all('div', class_='card') # 15 sites
    #print(len(arts))

    for art in arts:
        try:
            name = art.find('h6').text
        except:
            name = ''
        #print(name)

        try:
            url = art.find('h6').find('a').get('href')
        except:
            url = ''

        try:
            text = art.find('h4', class_='entry-title').text.strip() # clear # . ,
        except:
            text = ''
        try:
            year = art.find('span', class_='date').text.strip()
        except:
            year = ''

        data = {'name': name,
                'url': url,
                'text': text,
                'year': year}

        write_csv(data)


# several pages






def main():
    pattern = 'http://moveclick.ru/page/{}'  # 5 pages

    for i in range(0, 5):
        url = pattern.format(str(i)) # http://moveclick.ru/
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()

