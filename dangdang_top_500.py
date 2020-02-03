import requests
import re
import json


def work(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-'+str(page)
    html = request_dandan(url)  # 得到html
    items = parse_result(html)  # 解析过滤我们想要的信息
    # 写入txt
    for item in items:
        write_item_to_file(item)


def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def parse_result(html):
   # (.*?)  为所匹配的内容
   pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?' # 匹配排名
                        '<img src="(.*?)".*?' # 匹配图片地址
                        'class="name".*?title="(.*?)">.*?' # 书名
                        'class="star">.*?'
                        'class="tuijian">(.*?)</span>.*?' # 推荐指数
                        'class="publisher_info">.*?'
                        'target="_blank">(.*?)</a>.*?' # 匹配作者
                        'class="biaosheng">.*?'
                        '<span>(.*?)</span></div>.*?' # 五星好评次数
                        '<p><span\sclass="price_n">&yen;(.*?)</span>.*?' # 价格
                        '</li>',re.S)
   items = re.findall(pattern,html)
   for item in items:
       yield { # 每次遍历，每次返回
           'rank': item[0],
           'iamge': item[1],
           'title': item[2],
           'recommend': item[3],
           'author': item[4],
           'times': item[5],
           'price': item[6]
       }

def write_item_to_file(item):
   print('开始写入数据 ====> ' + str(item))
   with open('dangdang_top_book.txt', 'a', encoding='UTF-8') as f: # 以添加的方式写入txt
       f.write(json.dumps(item, ensure_ascii=False) + '\n') # json.dumps将字典转化为字符串
       f.close()


# 爬取前25页
for i in range(1,26):
    work(i)