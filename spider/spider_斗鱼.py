from selenium import webdriver
import requests
import time
import re

url = "https://www.douyu.com/g_LOL"
driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
# 滑动窗口，加载图片
for i in range(17):
    driver.execute_script("window.scrollBy(0, 500)")
    time.sleep(1)
# driver.find_element_by_xpath('class="Aside-toggle"')
info_list = driver.find_elements_by_xpath('//a[@class="DyListCover-wrap"]')
for info in info_list:
    name = info.find_element_by_xpath('.//h2[@class="DyListCover-user"]').text
    image_url = info.find_element_by_xpath('.//img[@src]').get_attribute("src")
    print(image_url)
    try:
        image_url = re.match(".*\.png", image_url).group()
    except:
        image_url = re.match(".*\.jpg", image_url).group()
    response = requests.get(image_url)

    print(name, image_url)
    with open("./douyu/" + name + ".png", "wb") as f:
        f.write(response.content)
driver.close()
