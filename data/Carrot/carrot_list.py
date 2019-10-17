from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

data_list = ["아이패드", "아이폰", "갤럭시s", "갤럭시노트", "갤럭시탭"]
cnt=0
driver = webdriver.Chrome("../chromedriver.exe")
driver.implicitly_wait(3)
for data in data_list:
    cnt+=1
    driver.get("https://www.daangn.com/search/"+data)
    
    # 더보기 버튼을 클릭해도 img_url이 다 가져와지지 않음..
    # 해결방안 : 고민중
    # #더보기 버튼 클릭
    # driver.find_element_by_class_name("more-btn").click()

    #상세페이지 연결 정보 가져오기
    request_data = {data:[]}
    driver1 = webdriver.Chrome("../chromedriver.exe")
    a_tag = driver.find_elements_by_class_name("flea-market-article-link")
    cnt1=1
    for a in a_tag:
        a_url = a.get_attribute("href")
        driver1.get(a_url)
        id = a_url.split("/")
        id = id[4]
        url_data = driver1.find_elements_by_class_name("image-wrap")
        for img in url_data:
            url = img.find_element_by_tag_name("img").get_attribute("src")
            if url==None:
                continue
            else:
                if cnt1%2==0:
                    title = driver1.find_elements_by_tag_name("h1")
                    title = title[2].text
                    price = driver1.find_element(By.ID, 'article-price')
                    price = price.text
                    description = driver1.find_element(By.ID, 'article-detail')
                    description = description.text
                    region = driver1.find_element(By.ID, "region-name").text
                    size = ""
                    if "기가" in description:
                        index = description.find("기가")
                        size = description[(index-3):index]
                    elif "16G" in description:
                        size = "16"
                    elif "32G" in description:
                        size = "32"
                    elif "64G" in description:
                        size = "64"
                    elif "128G" in description:
                        size = "128"
                    elif "256G" in description:
                        size = "256"
                    elif "512G" in description:
                        size = "512"
                    if len(size)==0:
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
                    if data == "아이패드" or data == "아이폰" :
                        company = "애플"
                    elif "갤럭시" in data :
                        company = "삼성전자"
                    request_data[data].append({
                        'id' : id,
                        'img_url': url,
                        'company' : company,
                        'title' : title,
                        'price' : price,
                        'region' : region,
                        'size' : size+"G",
                        'description' : description
                    })
                cnt1+=1
    #cnt는 주석 예정################################################
    if cnt==1:
        break
print(request_data)

    