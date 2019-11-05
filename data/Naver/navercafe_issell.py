from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import pymysql
import time
import requests
import json
conn = pymysql.connect(host='52.78.203.0', user='newuser', password='ssafy', db='junggobi', charset='utf8')
API_URL = "http://52.78.203.0:8000/api/"
headers = {'content-type': 'application/json'}
def test():
    curs = conn.cursor()

    chrome_options= webdriver.ChromeOptions() #옵션 설정하기
    # chrome_options.add_argument('headless') #창이 안보이도록 숨기기
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.3')
    driver = webdriver.Chrome("../chromedriver.exe",chrome_options=chrome_options)
    
    driver.implicitly_wait(3)
    driver.get('https://nid.naver.com/nidlogin.login')
    id = 'shy_red'
    pw = 'crldwusbf127!'
    # id = 'sjins0127'
    # pw = 'jso127!'
    driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    try :
        driver.find_element_by_css_selector('.btn_upload > .btn') # 에러가 발생할 가능성이 있는 코드
        driver.find_element_by_css_selector('.btn_upload > .btn').click()
    except:  
        pass  

    try:
        driver.find_element_by_css_selector('.btn_cancel3')
        driver.find_element_by_css_selector('.btn_cancel3').click()
    except:
        pass
    try:
        driver.find_element_by_css_selector('#fm > div > a')
        driver.find_element_by_css_selector('#fm > div > a').click()
    except:
        pass
    # #로그인 성공
    # urllib.request.urlretrieve(li[5],"../../.media/"+li[3]+".jpg" )
    # 'img_src': "http://52.78.203.0:8000/media/"+li[3]+".jpg",

    # sql = "UPDATE product_info SET is_sell=1 WHERE id="+primary_key[count]
    request_data = {'product_info': []}
    result = mysql()
    for cur in result:
        print("##############")
        print(cur)
        driver.get(cur['link'])
        try:
            driver.switch_to.frame('cafe_main')
            html = driver.page_source
            document = BeautifulSoup(html, 'html.parser')
            article = document.find_all(class_='sold_txt')
            if len(article) is 1:
                if "판매가 완료된 상품" in article[0].text:
                    saveDb(cur['id'])
                    print("판매완료")
            else:
                print("문제없음")
        except:
            print("게시글 삭제")
            saveDb(cur['id'])



def saveDb(id):
    cursor = conn.cursor()
    query = "UPDATE product_info SET is_sell= 1 WHERE id="+str(id)
    cursor.execute(query)
    conn.commit()

def mysql():
    cursor = conn.cursor()
    query = "select id,link from product_info where link like '%cafe.naver.com%' and date = '2019-11-3' and is_sell = 0"
    cursor.execute(query)
    row = dictfetchall(cursor)  
    return row

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

if __name__ == '__main__':
    test()
