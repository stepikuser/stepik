import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"

try:

	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	y_element = browser.find_element_by_id("answer")
	y_element.send_keys(y)
	checkbox = browser.find_element_by_id("robotCheckbox")
	checkbox.click()
	radiobutton = browser.find_element_by_id("robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
	radiobutton.click()

	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()
