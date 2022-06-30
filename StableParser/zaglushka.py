from selenium import webdriver
import time

def get_source_html(url):
    driver = webdriver.Chrome(executable_path=r"D:\PyCharm\Projects\StableParser\chromedriver.exe")
    driver.maximize_window()
    try:
        driver.get(url=url)
        time.sleep(3)
        i = 0
        while i < 1000:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            i += 1
        with open('index.html', 'w') as f:
            f.write(driver.page_source)


    except Exception as ex:
        print (ex)
    finally:
        driver.close()
        driver.quit()


def name(str):
    return print(str.split('/')[-1])

def funk():
   countrys = soup.find_all('span', class_="event__title--type")
    for item in countrys:
        print(item.text)
    leagues = soup.find_all('span', class_="event__title--name")
    for item in leagues:
        print(item.text)
    times = soup.find_all('div', class_="event__time")
    for item in times:
        print(item.text)
    time_home = soup.find_all('div', class_="event__participant event__participant--home")
    for item in time_home:
        print(item.text)
    time_away = soup.find_all('div', class_="event__participant event__participant--away")
    for item in time_away:
        print(item.text)
    coffs_1 = soup.find_all('div', class_="event__odd--odd1")
    for item in coffs_1:
        print(item.text)
    coffs_2 = soup.find_all('div', class_="event__odd--odd2")
    for item in coffs_2:
        print(item.text)
    coffs_3 = soup.find_all('div', class_="event__odd--odd3")
    for item in coffs_3:
        print(item.text)