import math
from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:

	browser = webdriver.Chrome()
	browser.get(link)
	fname = browser.find_element_by_name("firstname")
	fname.send_keys("kekek")
	lname = browser.find_element_by_name("lastname")
	lname.send_keys("kekek")
	email = browser.find_element_by_name("email")
	email.send_keys("kekek")
	element = browser.find_element_by_id("file")
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, '2.2.8.empty.txt')           # добавляем к этому пути имя файла 
	element.send_keys(file_path)

	button = browser.find_element_by_tag_name("button")
	button.click()
finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()
