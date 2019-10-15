from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(3)
driver.get('https://m.bunjang.co.kr/')

login_number = driver.find_element_by_class_name("input-wrapper")
login_number.find_element_by_name("phone").send_keys("01071193527")
password = driver.find_element_by_name("password").send_keys("junggobi1014!")
btn = driver.find_element_by_class_name("login-btn").click()

