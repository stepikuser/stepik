import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select




link = "http://suninjuly.github.io/selects2.html"

try:

	browser = webdriver.Chrome()
	browser.get(link)

	first_number = int(browser.find_element_by_id("num1").text)
	second_number = int(browser.find_element_by_id("num2").text)
	result = first_number + second_number
	Select(browser.find_element_by_id("dropdown")).select_by_value(str(result))	

	button = browser.find_element_by_css_selector("button.btn")
	button.click()
finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()
