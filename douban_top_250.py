import requests
from bs4 import BeautifulSoup
# 导入excel库
import xlwt

# 创建excel
book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建工作簿
sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
tags = ['名称', '图片', '排名', '评分', '作者', '简介']
# 写入第一行
for i in range(0, 6):
    sheet.write(0, i, tags[i])


def work(page):
    url = 'https://movie.douban.com/top250?start='+str(page*25)+'&filter='
    # 请求HTML
    html = request_douban(url)
    # 得到内容
    soup = BeautifulSoup(html, 'lxml')
    # 保存到excel
    save_to_excel(soup,page*25+1)

def request_douban(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def save_to_excel(soup,n):
    list = soup.find(class_='grid_view').find_all('li')
    print("=====")
    for item in list:
        print(n)
        item_name = item.find(class_='title').string
        sheet.write(n,0,item_name)
        item_img = item.find('a').find('img').get('src')
        sheet.write(n, 1, item_img)
        item_index = item.find(class_='').string
        sheet.write(n, 2, item_index)
        item_score = item.find(class_='rating_num').string
        sheet.write(n, 3, item_score)
        item_author = item.find('p').text
        sheet.write(n, 4, item_author)
        item_intr = item.find(class_='inq').string
        sheet.write(n,5,item_intr)
        n+=1





for i in range(0,10):
    work(i)

# 最后保存
book.save(r'豆瓣最受欢迎的250部电影.xlsx')