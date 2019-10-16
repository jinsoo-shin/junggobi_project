from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
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

    #상세페이지 연결 정복 가져오기
    driver1 = webdriver.Chrome("../chromedriver.exe")
    a_tag = driver.find_elements_by_class_name("flea-market-article-link")
    cnt1=1
    for a in a_tag:
        a_url = a.get_attribute("href")
        driver1.get(a_url)
        url_data = driver1.find_elements_by_class_name("image-wrap")
        for img in url_data:
            url = img.find_element_by_tag_name("img").get_attribute("src")
            if url==None:
                continue
            else:
                if cnt1%2==0:
                    print(url)
                    title = driver1.find_elements_by_tag_name("h1")
                    title = title[2].text
                    print(title)
                cnt1+=1
    if cnt==1:
        break

    