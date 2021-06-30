import math
from selenium import webdriver
import time




def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:

	browser = webdriver.Chrome()
	browser.get(link)

	alert_button = browser.find_element_by_tag_name("button")
	alert_button.click()
	alert = browser.switch_to_alert()
	alert.accept()

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	y_element = browser.find_element_by_id("answer")
	y_element.send_keys(y)
	
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	
	print(browser.switch_to_alert().text)
finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()
