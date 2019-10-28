from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pymysql
import time
import requests
import json

conn = pymysql.connect(host='192.168.100.60', user='newuser', password='ssafy',
                       db='junggobi', charset='utf8')
curs = conn.cursor()

API_URL = "http://localhost:8000/api/"
headers = {'content-type': 'application/json'}

#user agent 유저인척하여 막히지 않도록!!
chrome_options= webdriver.ChromeOptions() #옵션 설정하기
# chrome_options.add_argument('headless') #창이 안보이도록 숨기기
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.3')

driver = webdriver.Chrome("../chromedriver.exe",chrome_options=chrome_options)
driver.implicitly_wait(3)
driver.get('http://localhost:8000/api/product/?link=https://m.bunjang.co.kr/')

link_list = driver.find_elements_by_tag_name("a")
lit_list = driver.find_elements_by_class_name("lit")
driver1 = webdriver.Chrome("../chromedriver.exe",chrome_options=chrome_options)
primary_key = []
for i in range(3, len(lit_list),3):
    primary_key.append(lit_list[i].text)
# print(primary_key)


cnt = False
count = 0
test=0
request_data = {'product_info': []}
for l_l in link_list:
    link = l_l.text
    if "m.bunjang" in link:
        print(link)
        driver1.get(link)
        # time.sleep(3)
        # # #번개장터 접속 후, 로그인
        try:
            if cnt==False:
                login_number = driver1.find_element_by_class_name("sc-cQFLBn")
                login_number.find_element_by_tag_name("input").send_keys("01071193527")
                password = driver1.find_element_by_class_name("sc-gojNiO")
                password.find_element_by_tag_name("input").send_keys("junggobi1014!")
                btn = driver1.find_element_by_class_name("sc-daURTG").click()
            html = driver1.page_source
            soup = BeautifulSoup(html, "html.parser")
            sell = soup.select("#root > div > div > div.sc-gJqsIT.hbVxbC > div.sc-kDhYZr.ikrBOB > div > div.sc-hcnlBt.jfMCiR > div > div.sc-iHhHRJ.gVVJLD > div > div.sc-gPzReC.fWxkCf > div.sc-jrIrqw.hOgugl > div.sc-hjRWVT.bbGQaP")
            sell[0].text
            cnt=True
        except:
            print("판매완료")
            sql = "UPDATE product_info SET is_sell=1 WHERE id="+primary_key[count]
            curs.execute(sql)
            conn.commit()
            print(sql)
            continue
            # break
        count+=1
conn.close()