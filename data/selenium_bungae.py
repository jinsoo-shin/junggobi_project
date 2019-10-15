from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen

driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(3)
driver.get('https://m.bunjang.co.kr/')

#번개장터 접속 후, 로그인
login_number = driver.find_element_by_class_name("input-wrapper")
login_number.find_element_by_name("phone").send_keys("01071193527")
password = driver.find_element_by_name("password").send_keys("junggobi1014!")
btn = driver.find_element_by_class_name("login-btn").click()

#아이패드 검색
search = driver.find_element_by_class_name("search-box")
search.find_element_by_class_name("search-box-input").send_keys("아이패드")
search.find_element_by_class_name("search-box-input").send_keys(Keys.RETURN)

#아이패드 리스트 찾기
u_list = driver.find_element_by_class_name("category-product-list").find_elements_by_tag_name("img")
url_list = []
for i in u_list:
    src = i.get_attribute("data-src")
    src = src.split("https://seoul-p-studio.bunjang.net/product/")
    src = src[1][0:9]
    if src[8]=="_":
        src = src[0:8]
    url_list.append(src)
print(url_list)
print(len(url_list))

#상세페이지 웹 크롤링
# for data in url_list:
    # url = https://m.bunjang.co.kr/products/109068073?ref=%EA%B2%80%EC%83%89%EA%B2%B0%EA%B3%BC&q=%EC%95%84%EC%9D%B4%ED%8C%A8%EB%93%9C,