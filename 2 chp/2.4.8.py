import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time





def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:

	browser = webdriver.Chrome()
	browser.get(link)

	buy_button = browser.find_element_by_id("book")
	WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	buy_button.click()

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	y_element = browser.find_element_by_id("answer")
	y_element.send_keys(y)
	button = browser.find_element_by_id("solve")
	button.click()
	
	print(browser.switch_to_alert().text)
finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()
