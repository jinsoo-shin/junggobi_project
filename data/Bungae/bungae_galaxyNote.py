from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen

driver = webdriver.Chrome("../chromedriver.exe")
driver.implicitly_wait(3)
driver.get('https://m.bunjang.co.kr/')

#번개장터 접속 후, 로그인
login_number = driver.find_element_by_class_name("input-wrapper")
login_number.find_element_by_name("phone").send_keys("01071193527")
password = driver.find_element_by_name("password").send_keys("junggobi1014!")
btn = driver.find_element_by_class_name("login-btn").click()

#아이폰 검색
search = driver.find_element_by_class_name("search-box")
search.find_element_by_class_name("search-box-input").send_keys("갤럭시노트")
search.find_element_by_class_name("search-box-input").send_keys(Keys.RETURN)

#아이폰 리스트 찾기
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
    url = "https://m.bunjang.co.kr/products/"+data+"?ref=검색결과&q=갤럭시노트"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    sell = soup.select("#app > div.router-view > div > div.product-detail-wrapper > div:nth-child(2) > div:nth-child(1) > div.suggested-products-title")
    if len(sell)==0:
        title = soup.find_all("h2")
        price = soup.find_all("h3")
        status = soup.select("ul.product-summary__assistant-2nd>li.status")
        exchange = soup.select("ul.product-summary__assistant-2nd>li.exchange")
        shipping = soup.select("ul.product-summary__assistant-2nd>li.shipping")
        location = soup.select("ul.product-summary__assistant-2nd>li.location")
        description = soup.find_all("p")
        id = data
        size = ""
        title = title[0].text.strip()
        print(title)
        if "매입" not in title:
            cnt+=1
            if "기가" in title:
                index = title.find("기가")
                size = title[(index-3):index]
            elif "16G" in title:
                size = "16"
            elif "32G" in title:
                size = "32"
            elif "64G" in title:
                size = "64"
            elif "128G" in title:
                size = "128"
            elif "256G" in title:
                size = "256"
            elif "512G" in title:
                size = "512"

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
                'company' : "삼성전자",
                'title' : title,
                'price' : price,
                'status' : status,
                'exchange' : exchange,
                'shipping' : shipping,
                'region' : location,
                'size' : size+"G",
                'description' : description
            })
        #cnt 주석 예정#####################
        if cnt==1:
            break
    else:
        print("상품이 판매되었습니다.")
print(request_data)
    
