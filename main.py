import os
import time
import requests
from bs4 import BeautifulSoup
from progress.bar import IncrementalBar

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.148 YaBrowser/22.7.2.899 Yowser/2.5 Safari/537.36"
}

first_list_of_src = []
second_list_of_src = []

def download(list, rr, limit):
    global headers
    numb = 1000
    path = ''
    os.system('cls')
    if rr == '2':
        path = os.getcwd() + '\\' + 'dataset' + '\\' + 'download_data' + '\\' + 'bay horse'
        print('Bay horse download:')
    if rr == '1':
        path = os.getcwd() + '\\' + 'dataset' + '\\' + 'download_data' + '\\' + 'zebra'
        print('Zebra download:')
    bar = IncrementalBar('Progress', max = limit)
    for p in list:
        r = requests.get('https:' + p, headers = headers)
        if numb < 2000:
            num = str(numb)[1:4]
            num = '0' + num
        else:
            num = str(numb - 1000)
        f = open(path + '\\' + num + '.jpg', 'wb')
        f.write(r.content)
        f.close()
        bar.next()
        numb += 1
        time.sleep(1)

def bay_horse(limit):
    global second_list_of_src
    num_page = 0
    print("Getting links of bay horse:")
    bar = IncrementalBar('Progress', max= limit)

    while True:
        second_url = f"https://yandex.ru/images/search?p={num_page}&from=tabbar&text=bay%20horse&lr=51&rpt=image&uinfo=sw-1920-sh-1080-ww-1220-wh-970-pd-1-wp-16x9_1920x1080"
        num_page += 1

        second_response = requests.get(second_url, headers=headers)
        second_soup = BeautifulSoup(second_response.content, 'lxml')
        r = second_soup.find_all('img', class_= 'serp-item__thumb')

        for link in r:
            if len(second_list_of_src) >= limit:
                bar.finish()
                os.system('cls')
                download(second_list_of_src, str(2), limit)
                return
            second_list_of_src.append(link['src'])
            bar.next()
            time.sleep(0.1)
        time.sleep(2)


def zebra(limit):
    global first_list_of_src
    num_page = 0
    print("Getting links of zebra:")
    bar = IncrementalBar('Progress', max= limit)


    while True:
        first_url = f"https://yandex.ru/images/search?p={num_page}&text=zebra&uinfo=sw-1536-sh-864-ww-760-wh-754-pd-1.25-wp-16x9_1920x1080&lr=51&rpt=image"
        num_page += 1

        first_response = requests.get(first_url, headers=headers)
        first_soup = BeautifulSoup(first_response.content, 'lxml')

        r = first_soup.find_all('img', class_= 'serp-item__thumb')

        for link in r:
            if len(first_list_of_src) >= limit:
                bar.finish()
                os.system('cls')
                bay_horse(limit)
                download(first_list_of_src, str(1), limit)
                return
            first_list_of_src.append(link['src'])
            bar.next()
            time.sleep(0.1)
        time.sleep(2)

if __name__ == "__main__":
    print('Enter the limit of uploaded images:')
    limit1 = input()

    path_file = os.getcwd() + "\\" + 'dataset'

    if os.path.exists(path_file):
        pass
    else:
        os.mkdir(path_file)

    path_file = path_file + '\\' + 'download_data'

    if os.path.exists(path_file):
        pass
    else:
        os.mkdir(path_file)

    if os.path.exists(path_file + '\\' + 'zebra'):
        pass
    else:
        os.mkdir(path_file + '\\' + 'zebra')

    if os.path.exists(path_file + '\\' + 'bay horse'):
        pass
    else:
        os.mkdir(path_file + '\\' + 'bay horse')

    os.system('cls')
    zebra(int(limit1))
    os.system('cls')
    print("Finished")