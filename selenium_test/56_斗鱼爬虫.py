import re
import time
import requests
from selenium import webdriver

# url = re.match(".*\.jpg",url).group()
# driver.maximize_window()
# driver.execute_script("window.scrollBy(250, 500)")
# 1.准备url
url = 'https://www.douyu.com/g_yz'
# 2.发送请求
driver = webdriver.Chrome()
driver.get(url)
# 3.让页面加载
time.sleep(2)
driver.maximize_window()
driver.execute_script("window.scrollBy(250, 500)")
for i in range(16):
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 500)")
# 4.获取图片的url和主播名字
lis = driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li')
for li in lis:
    url = li.find_element_by_xpath('.//img[@class="DyImg-content is-normal "]').get_attribute("src")
    name = li.find_element_by_xpath('.//h2[@class="DyListCover-user"]').text
    try:
        url = re.match(".*\.jpg", url).group()
        response = requests.get(url)
        with open("./img/" + name + ".jpg", 'wb') as f:
            f.write(response.content)
    except:
        url = re.match(".*\.png", url).group()
        response = requests.get(url)
        with open("./img/" + name + ".png", 'wb') as f:
            f.write(response.content)

# 5处理url和主播名爬取图片并保存
# 将图片写到相应的文件夹内
# 图片的名字叫做主播名
# 6.翻页

driver.close()
