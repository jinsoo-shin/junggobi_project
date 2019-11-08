from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import urllib.request
import re
import csv
import regex_function
import json
import datetime
API_URL = 'http://52.78.203.0:8000/api/'
headers = {'content-type': 'application/json'}
filename = 'navercafe_passtext.txt'
passtext = []
with open(filename, mode='r', encoding='utf-8') as data:
    passtext = data.readlines()
    passtext = [x.strip('\n') for x in passtext]

chrome_options= webdriver.ChromeOptions() #옵션 설정하기
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('headless') #창이 안보이도록 숨기기
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.3')
driver = webdriver.Chrome("./chromedriver",chrome_options=chrome_options)
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
id = 'sjins0127'
pw = 'jso127!'
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
#로그인 성공


page_number = 1
list = []
search_url_list=[]
search_url_list.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=10050146&search.menuid=339&search.media=0&search.searchdate=all&search.defaultValue=1&search.exact=&search.include=&userDisplay=15&search.exclude=&search.onSale=1&search.option=3&search.sortBy=date&search.searchBy=1&search.searchBlockYn=0&search.includeAll=&search.query=%BE%C6%C0%CC%C6%F9&search.viewtype=title&search.page=")#SKT
search_url_list.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=10050146&search.menuid=424&search.media=0&search.searchdate=all&search.defaultValue=1&search.exact=&search.include=&userDisplay=15&search.exclude=&search.onSale=1&search.option=3&search.sortBy=date&search.searchBy=1&search.searchBlockYn=0&search.includeAll=&search.query=%BE%C6%C0%CC%C6%F9&search.viewtype=title&search.page=")#KT
search_url_list.append("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=10050146&search.menuid=425&search.media=0&search.searchdate=all&search.defaultValue=1&search.exact=&search.include=&userDisplay=15&search.exclude=&search.onSale=1&search.option=3&search.sortBy=date&search.searchBy=1&search.searchBlockYn=0&search.includeAll=&search.query=%BE%C6%C0%CC%C6%F9&search.viewtype=title&search.page=")#LGU+
for search_url_page in search_url_list:
    for page_num in range(page_number):
        search_url=search_url_page+str(page_num+1)
        driver.get(search_url)
        driver.implicitly_wait(3)
        driver.switch_to.frame('cafe_main')
        html = driver.page_source
        dom = BeautifulSoup(html, 'html.parser')
        dom1 = dom.find_all(class_='td_article')
        cafeurl = "https://cafe.naver.com"
        for element in dom1:

            # try:
            #     is_sell=element.find(class_="list-i-sellout").text
            #     if "완료" in is_sell:
            #         continue
            # except:
            #     pass
            a = element.find('a')
            title = a.get_text(strip=True)
            if "아이폰" not in title:
                continue

            if any(format in title for format in passtext):
                continue # 만약 passtext의 문자열을 title이 포함하고 있다면 넘긴다!
            else:
                element_url=cafeurl+a.get('href')
                list.append(element_url)
        
        ######

save_result = []
for i in range(len(list)):
    result =[]
    info_url=list[i]
    try:
        driver.get(info_url)
        driver.implicitly_wait(3)
        driver.switch_to.frame('cafe_main')
        html = driver.page_source
        page = BeautifulSoup(html, 'html.parser')
        inbox = page.find(class_="inbox")
        tt = page.find(id="tbody")
        img_src = tt.find(class_="image_condition").find("img").get('src')
        # img_src = img_src.replace("?type=s3","").replace("%3Ftype%3Df1","")
        is_sell = False
        try:
            is_sell_text = tt.find(class_="image_condition").find(class_="sold_txt").text
            if "판매가 완료된 상품" in is_sell_text:
                is_sell = True
        except:
            pass
        date = page.find(class_="tit-box").find(class_="date").text
        regex = re.compile(r"articleid=(\d+)&")
        mc = regex.search(info_url)

        id=mc.group(1)#아이디
        simple_url = "https://cafe.naver.com/joonggonara/"+mc.group(1)

        read_title = tt.find(class_="title").text
        read_price = tt.find(class_="cost").text
        test = tt.find_all(string=True)
        index = None
        text =[]
        for i in range(len(test)):
            if "해외직구로 면세" in test[i]:
                index = i
                break
        test = test[index+1:]
        text.append(" ".join(test).strip())
        read_text = " ".join(text).replace('\xa0','').replace('\xa9','').replace("\n"," ").replace("  "," ")#텍스트
        # if any(format in read_text for format in passtext):
        #     continue # 만약 passtext의 문자열을 read_text가 포함하고 있다면 넘긴다!
        result.append(read_title)
        result.append(read_price)
        result.append(read_text)
        result.append(id)
        result.append(date)#날짜
        result.append(img_src)#이미지 주소
        result.append(simple_url)
        result.append(is_sell)

        save_result.append(result)
    except:
        continue


request_data = {'navercafe': []}
for li in save_result:
    read_title=li[0]
    read_price=li[1]
    read_text=li[2]
    product={}
    product= regex_function.get_iphone_model(product,read_title,read_text)
    product =regex_function.get_price(product,read_title,read_price,read_text)
    #사진 저장하기
    urllib.request.urlretrieve(li[5],"../../.media/"+li[3]+".jpg" )
    # 타이틀, 가격, 내용, 아이디, 날짜, 이미지주소, 링크
    request_data['navercafe'].append({
        'category' : '모바일',
        'manufacturer' : '애플',
        'model_name': product['model_name'],
        'storage': product['storage'],
        'price': str(product['price']),
        'id': li[3],
        'date': li[4],
        'img_src': "http://52.78.203.0:8000/media/"+li[3]+".jpg",
        'link': li[6],
        'title':li[0],
        'contents':li[2],
        'is_sell':li[7]
        })
response = requests.post(API_URL + 'product/', data=json.dumps(request_data), headers=headers)
 
