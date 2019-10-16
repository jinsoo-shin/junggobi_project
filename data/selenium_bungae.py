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

#상세페이지 웹 크롤링
cnt=0
request_data = {'bungae': []}
for data in url_list:
    cnt+=1
    url = "https://m.bunjang.co.kr/products/"+data+"?ref=%EA%B2%80%EC%83%89%EA%B2%B0%EA%B3%BC&q=%EC%95%84%EC%9D%B4%ED%8C%A8%EB%93%9C"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find_all("h2")
    price = soup.find_all("h3")
    status = soup.select("ul.product-summary__assistant-2nd>li.status")
    exchange = soup.select("ul.product-summary__assistant-2nd>li.exchange")
    shipping = soup.select("ul.product-summary__assistant-2nd>li.shipping")
    location = soup.select("ul.product-summary__assistant-2nd>li.location")
    description = soup.find_all("p")
    id = data
    title = title[0].text.strip()
    cellular = False
    if "셀룰러" in title:
        cellular = True
    elif "cellular" in title:
        cellular = True
    elif "Cellular" in title:
        cellular = True
    if "기가" in title:
        index = title.find("기가")
        size = title[(index-3):index]
    elif "32G" in title:
        size = "32G"
    elif "64G" in title:
        size = "64G"
    elif "128G" in title:
        size = "128G"
    elif "256G" in title:
        size = "256G"
    elif "512G" in title:
        size = "512G"

    price = price[0].text.strip()
    status = status[0].find("span").text
    exchange = exchange[0].find("span").text
    shipping = shipping[0].find("span").text
    location = location[0].find("span").text.strip()
    location = location.split("\n")
    location = location[0]
    description = description[0].text

    request_data['bungae'].append({
        'id' : data,
        'title' : title,
        'price' : price,
        'status' : status,
        'exchange' : exchange,
        'shipping' : shipping,
        'region' : location,
        'cellular' : cellular,
        'size' : size,
        'description' : description
    })
    #cnt 주석 예정#####################
    if cnt==1:
        break
print(request_data)
    