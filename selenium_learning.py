from selenium import webdriver
# 创建了一个 Chrome 驱动
driver = webdriver.Chrome()
# 使用 get 方法打开百度
driver.get("https://www.baidu.com")

# 获取到输入框之后我们就往里面写入我们要搜索的内容
input = driver.find_element_by_css_selector('#kw')
input.send_keys("linese")
# 获取到搜索这个按钮 然后点击
button = driver.find_element_by_css_selector('#su')
button.click()

# 爬完之后要关闭
# driver.close()