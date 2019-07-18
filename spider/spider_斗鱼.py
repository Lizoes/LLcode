from selenium import webdriver
import time

url = "https://www.douyu.com/g_LOL"
driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
time.sleep(2)
# driver.find_element_by_xpath('class="Aside-toggle"')
info_list = driver.find_elements_by_xpath('//a[@class="DyListCover-wrap"]')
for info in info_list:
    text_list = info.text.split("\n")
    name = text_list[3]
    number = text_list[2]
    print(name, number)

