import requests
import lxml
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

u = UserAgent()
useragent = u.random

def get_data(urls):
    u = UserAgent()
    useragent = u.random
    headers = {
        "user-agent": useragent
    }
    #Далее то что нужно спарсить
    Page_count = 3

    #переход по страницам
    for page in range(1, Page_count + 1):
        url = f'https://doramy.club/page/{page}'
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        #снова парсинг страници вставить нужные объекты
        blocks = soup.find_all("div", class_="post-home")
        for block in blocks:
            urls = block.find("a").get('href')
            img = block.find("img").get('src')
            title = block.find("span").text
            print(f"\n\n{urls}: {title} --> {img}", end="")
            tables = block.find("tbody", class_="tbody-hom")
            for table in tables:
                for stat in table:
                    for s in stat:
                        print(f"{s}")
def main():
    get_data("https://doramy.club")

if __name__ == '__main__':
    main()