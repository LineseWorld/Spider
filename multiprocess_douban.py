import requests
from bs4 import BeautifulSoup
# 导入excel库
from multiprocessing import Pool
import multiprocessing
import os

def work(url):
    # 请求HTML
    html = request_douban(url)
    # 得到内容
    soup = BeautifulSoup(html, 'lxml')
    # 保存到excel
    save_to_excel(soup,url)

def request_douban(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def save_to_excel(soup,url):
    list = soup.find(class_='grid_view').find_all('li')
    filename = '多线程-豆瓣\\'+ url[35:41]+'.txt'
    with open(filename , 'w',encoding='utf-8') as f:
        for item in list:
            item_name = item.find(class_='title').string
            item_index = item.find(class_='').string
            item_score = item.find(class_='rating_num').string
            item_author = item.find('p').text
            item_intr = item.find(class_='inq').string
            data = "排名：" + item_index + " -- 影名：" + item_name + " -- 简介：" + item_intr + "\n"
            # print(url[35:41]) 判断是否有多线程运行
            f.write(data)

    f.close()

if __name__ == '__main__':
    # os.mkdir("多线程-豆瓣")
    # =================
    # 多线程处理
    urls = []
    # 根据电脑cup数创建线程池大小
    pool = Pool(multiprocessing.cpu_count())
    for i in range(0,10):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
        urls.append(url)

    pool.map(work, urls)
    pool.close()
    pool.join()
    # =================

