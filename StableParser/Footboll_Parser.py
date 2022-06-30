import requests
import simplejson as json
import xlsxwriter
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
u = UserAgent()
useragent = u.random
headers = {
    "user-agent": useragent
}
opts = webdriver.ChromeOptions()
opts.headless = True
driver = webdriver.Chrome(executable_path=r"D:\PyCharm\Projects\StableParser\chromedriver.exe", options=opts)
driver.implicitly_wait(60)
driver.maximize_window()

def get_source_html(url):
    try:
        print("Начался процесс сбора данных ...")
        name = url.split('/')[-1]
        driver.get(url=url)
        #############
        cockie_button = driver.find_element(By.ID,'customCookieAccept')
        cockie_button.click()
        time.sleep(1)
        tomorrow = driver.find_element(By.XPATH, '//*[@id="live-table"]/div[1]/div[2]/div/div[3]')
        tomorrow.click()
        time.sleep(1)
        kefe = driver.find_element(By.XPATH, '//*[@id="live-table"]/div[1]/div[1]/div[3]/div')
        kefe.click()
        deadline = time.monotonic() + 60
        while time.monotonic() < deadline:
            try:
                next = driver.find_element(By.XPATH, '//div[@title="Показать все игры этого турнира!"]')
                next.click()
                with open(f'{name}.html', 'w', encoding="utf-8") as f:
                    f.write(driver.page_source)
            except Exception as ex:
                continue
            time.sleep(1)
    except Exception as ex:
        print (ex)
    finally:
        driver.close()
        driver.quit()
    print("Процесс завершен. Начинаю обработку данных ...")

def get_data(filename="www.flashscore.ru.com"):
    with open(f"{filename}.html", encoding='utf-8') as file:
        response = file.read()
    soup = BeautifulSoup(response, 'html.parser')
    countrys = soup.find_all('span', class_="event__title--type")
    leagues = soup.find_all('span', class_="event__title--name")
    times = soup.find_all('div', class_="event__time")
    time_home = soup.find_all('div', class_="event__participant event__participant--home")
    time_away = soup.find_all('div', class_="event__participant event__participant--away")
    coffs_1 = soup.find_all('div', class_="event__odd--odd1")
    coffs_2 = soup.find_all('div', class_="event__odd--odd2")
    coffs_3 = soup.find_all('div', class_="event__odd--odd3")
    with xlsxwriter.Workbook(filename) as workbook:
        ws = workbook.add_worksheet()
        bold = workbook.add_format({'bold':True})

        headers = ['Страна', 'Лига', 'Время', 'Команда1', 'Команда2', '1', 'Х', '2']

        for col, h in enumerate(headers):
            ws.write_string(0, col, h, cell_format=bold)

        

    ##########

#ToDo СДЕЛАТЬ ПРАВИЛЬНУЮ ЗАПИСЬ И СОРТИРОВКУ ПОЧЕННЫХ ДАННЫХ
def dump_to_xlsx(filename, data):
    if not len(data):
        return None
    with xlsxwriter.Workbook(filename) as workbook:
        ws = workbook.add_worksheet()
        bold = workbook.add_format({'bold':True})

        headers = ['Страна', 'Лига', 'Время', 'Команда1', 'Команда2', '1', 'Х', '2']

        for col, h in enumerate(headers):
            ws.write_string(0, col, h, cell_format=bold)

        for row, item in enumerate(data, start=1):
            ws.write_string(row, 0, item["country"])
            ws.write_string(row, 1, item["league"])
            ws.write_string(row, 2, item["time"])
            ws.write_string(row, 3, item["team_one"])
            ws.write_string(row, 4, item["team_two"])
            ws.write_string(row, 5, item["coff_1"])
            ws.write_string(row, 6, item["coff_x"])
            ws.write_string(row, 7, item["coff_2"])
def main():
    #get_source_html('https://www.flashscore.ru.com')
    get_data()

if __name__ == '__main__':
    main()
