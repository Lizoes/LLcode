from selenium import webdriver
import time


# 设置浏览器模式
option = webdriver.ChromeOptions()
option.headless = True          # 最后使用，无头模式，不弹出浏览器


driver = webdriver.Chrome()     # 类似于reqeust
driver.maximize_window()        # 浏览器窗口最大化
driver.get("https://www.baidu.com/")   # drive本身又是一个response
driver.execute_script("window.scrollBy(左右，上下)")         # 浏览器下拉条，相对当前位置向下拉
# 使用driver操作
input_element = driver.find_element_by_id("kw")
submit_element = driver.find_element_by_id("su")
input_element.send_keys("python")           # 在输入框中填入文字
submit_element.click()                      # 点击按钮

# 浏览器设置


time.sleep(2)
driver.close()
