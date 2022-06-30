import requests
import lxml
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from Setings import *

u = UserAgent()
useragent = u.random
titles = []
categories = []
hrefs = []
urls = []

def get_data(url):
    u = UserAgent()
    useragent = u.random
    headers = {
        "user-agent": useragent
    }

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    #снова парсинг страници вставить нужные объекты
    blocks = soup.find_all("div", class_="production_item_title")
    for block in blocks:
        title = block.find('a').text
        href = block.find('a').get('href')
        #hrefs.append(href)
        titles.append(title)

    blocks_table = soup.find_all("div", class_="production_item_list")
    for block_table in blocks_table:
        for table_tag_ul in block_table:
            for table_tag_li in table_tag_ul:
                category = table_tag_li.find('a')
                hrefss = table_tag_li.find('a')
                if type(hrefss)!=int:
                    href = hrefss.get('href')
                    hrefs.append(href)
                if type(category)!=int:
                    categories.append(category.get_text())

    for href in hrefs:
        full_href = 'https://ventilator.spb.ru'+str(href)
        urls.append(full_href)
    
    parse_info_goods(urls)

def parse_info_goods(urls):
    u = UserAgent()
    useragent = u.random
    headers = {
        "user-agent": useragent
    }
    for url in urls:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        names = soup.find_all('div', class_="subcategory_block_name")
        for name_t in names:
            name = name_t.find('a').text

        infos = soup.find_all('div', class_="subcategory_block_text")
        for info_t in infos:
            info = info_t.text







def main():
    get_data(DOMAIN)
    print(titles)
    print(categories)
if __name__ == '__main__':
    main()