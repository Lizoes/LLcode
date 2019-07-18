from selenium import webdriver
import time

url = "https://www.douyu.com/g_LOL"
driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
time.sleep(3)
# driver.find_element_by_xpath('class="Aside-toggle"')
info_list = driver.find_elements_by_xpath('//a[@class="DyListCover-wrap"]')
i=1
for info in info_list:
    # text_list = info.text.split("\n")
    # name = text_list[3]
    # number = text_list[2]
    # print(name, number)
    name = info.find_element_by_xpath('.//h2[@class="DyListCover-user"]').text
    image = info.find_element_by_xpath('.//img[@src]').get_attribute("src")
    print(image)
driver.close()
