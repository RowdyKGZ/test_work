import requests
from bs4 import BeautifulSoup

urls = ''
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
           'accept': '*/*'}


def get_url(some_url):
    """Получение уникального урла и переопределение urls"""
    global urls
    urls = 'https://' + some_url


def get_html(url):
    """парсинг все страницы и перевод в BS4"""
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        response = response.text
        soup = BeautifulSoup(response, 'html.parser')
        return soup
    else:
        print('Статус код не 200')


def get_title_page_info(html_text):
    """Получаем тайтл"""
    title = html_text.find('title')
    return title.text


def get_meta_page_info(html_text):
    """Получаем мету страницы"""
    all_meta = html_text.find_all('meta')
    meta = ''
    for meta in all_meta:
        if str(meta).startswith('<meta charset'):
            meta = str(meta).split('"')[1]
            return meta
    return 'К сожалению мета не нашлась'


def get_h1_page_info(html_text):
    """Получение H1 страницы"""
    h1 = html_text.find('h1')
    if h1:
        return h1
    else:
        return 'h1 атрибута нету'


def parser(some_url):
    """основной запуск программы"""
    get_url(some_url)
    html_text = get_html(urls)
    title_page_info = get_title_page_info(html_text)
    meta_page_info = get_meta_page_info(html_text)
    h1_page_info = get_h1_page_info(html_text)
    print(title_page_info)
    print()
    print(meta_page_info)
    print()
    print(h1_page_info)
