import requests
import simplejson as json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
import time


u = UserAgent()
useragent = u.random
links = []
links_video = []
links_image = []
jsons = []

def get_data(urls):
    u = UserAgent()
    useragent = u.random
    headers = {
        "user-agent": useragent
    }
    for url in urls:
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        search_link_in_all_video = soup.find('div', class_="module clear video_module _module")
        link_in_all_video = search_link_in_all_video.find('a').get('href')
        link = f'https://vk.com{link_in_all_video}'
        links.append(link)
    get_source_html(links)

def get_source_html(urls):
    opts = webdriver.ChromeOptions()
    opts.headless = True
    driver = webdriver.Chrome(executable_path=r"D:\PyCharm\Projects\StableParser\chromedriver.exe", options=opts)
    driver.maximize_window()
    try:
        print("Начался процесс сбора данных ...")
        for url in urls:
            name = url.split('/')[-1]
            driver.get(url=url)
            time.sleep(3)
            i = 0
            while i < 100:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                i += 1
            with open(f'{name}.html', 'w', encoding="utf-8") as f:
                f.write(driver.page_source)
            time.sleep(3)
    except Exception as ex:
        print (ex)
    finally:
        driver.close()
        driver.quit()
        print('Сбор данных завершен. Начался процесс сбора ссылок ...')
    get_link_video(links)
    
def get_link_video(urls):
    for url in urls:
        name = url.split('/')[-1]
        with open(f"{name}.html", encoding='utf-8') as file:
            response = file.read()
        soup = BeautifulSoup(response, 'html.parser')
        video_blocks = soup.find_all('div', id="video_all_list")
        num = 1
        for block in video_blocks:
            srcs = block.find_all('div', attrs={"data-thumb": True})
            for src in srcs:
                tegs_a = src.find_all('a', class_="VideoCard__thumbLink video_item__thumb_link")
                images = src["data-thumb"]
                if images not in links_image:
                    links_image.append(images)
                    print(f'URL {num} successfully!')
                else:
                    links_image.append("image_url is not")
                    print(f"URL {num} bad? возможно видео удалено!")
                num += 1
                for teg_a in tegs_a:
                    link_video = f'https://vk.com{teg_a.get("href")}'
                    if link_video not in links_video:
                        if link_video != url:
                            links_video.append(link_video)
                    else:
                        continue
    print ("Ссылки собраны. Всего собраны:")
    print(f'Всего видео: {len(links_video)}, Всего картинок: {len(links_image)}')
    print('Начинаю сохранение...')
    save_result(links_image)

def save_result(arr):
    for i in range(len(arr)):
        video_and_image = {
            'Video_url': links_video[i],
            'Image_url': links_image[i]
        }
        jsons.append(video_and_image)

def main():
    try:
        get_data(['https://vk.com/renminribao'])
    except Exception as ex:
        print(ex, "Возможно в данной группе нет вкладки с видеозаписями или Нужно просто перезапустить парсер.")
    finally:
        with open('urls.json', 'w') as file:
            json.dump(jsons, file, indent=4, ensure_ascii=False)
            print (f"Данные сохранены в urls.json")
if __name__ == '__main__':
    main()
