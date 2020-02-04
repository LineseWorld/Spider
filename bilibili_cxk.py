import requests
from bs4 import BeautifulSoup
# 导入excel库
import xlwt
# 创建excle

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
tags = ['链接', '视频名称', '观看', '弹幕', '时间', 'up主']
for i in range(0,6):
    sheet.write(0,i,tags[i])
n = 1

def work(page):
    url = 'https://search.bilibili.com/all?keyword=%E8%94%A1%E5%BE%90%E5%9D%A4%20%E7%AF%AE%E7%90%83&from_source=nav_search_new&page='+str(page)
    # 获取html
    html = requests_bilibili(url)
    # 得到内容

    soup = BeautifulSoup(html,'lxml')
    # 保存到excel
    save_to_excel(soup)


def requests_bilibili(url):
    try:
        response = requests.get(url)
        print("response.status_code=",response.status_code)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def save_to_excel(soup):
    list  = soup.find(class_='video-list clearfix').find_all('li')
    global n
    for item in list:
        item_link = item.find('a').get('href')
        sheet.write(n, 0, item_link)
        item_name = item.find(class_='title').get_text()
        sheet.write(n, 1, item_name)
        item_look = item.find(class_='so-icon watch-num').get_text()
        sheet.write(n, 2, item_look)
        item_danmu = item.find(class_='so-icon hide').get_text()
        sheet.write(n, 3, item_danmu)
        item_time = item.find(class_='so-icon time').get_text()
        sheet.write(n, 4, item_time)
        item_up_name = item.find(class_='up-name').string
        sheet.write(n, 5, item_up_name)
        n = n+1


for i in range(1,11):
    work(i)

book.save("B站蔡徐坤篮球视频.xlsx")