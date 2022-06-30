import requests
import lxml
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from Setings import *

u = UserAgent()
useragent = u.random

def get_data(url):
    u = UserAgent()
    useragent = u.random
    headers = {
        "user-agent": useragent
    }

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    #Далее то что нужно спарсить
    Page_count = PAGE_COUNT

    #переход по страницам
    for page in range(1, Page_count + 1):
        url = f'{PAGINATION}{page}'
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        #снова парсинг страници вставить нужные объекты
        title = TITLE
        info = INFO
        price = PRICE


def main():
    get_data(DOMAIN)

if __name__ == '__main__':
    main()
