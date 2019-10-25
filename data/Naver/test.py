from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import urllib.request
import re
import csv
import pandas as pd
import regex_function
import json
import datetime
API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}
filename = 'navercafe_passtext.txt'
passtext = []
with open(filename, mode='r', encoding='utf-8') as data:
    passtext = data.readlines()
    passtext = [x.strip('\n') for x in passtext]
    print(passtext)
    ##파일읽어와서 리스트로 만들었음

# savefile = 'navercafe-crawling.txt'

# f = open(savefile, mode='a', encoding='utf-8')

chrome_options= webdriver.ChromeOptions() #옵션 설정하기
# chrome_options.add_argument('headless') #창이 안보이도록 숨기기
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.3')
driver = webdriver.Chrome("../chromedriver.exe",chrome_options=chrome_options)
driver.implicitly_wait(3)
# driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
id = 'sjins0127'
pw = 'jso127!'
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

try :
    driver.find_element_by_css_selector('.btn_upload > .btn') # 에러가 발생할 가능성이 있는 코드
    driver.find_element_by_css_selector('.btn_upload > .btn').click()
except:  # 에러 종류
    pass #에러가 발생 했을 경우 처리할 코드

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
for page_num in range(page_number):
    search_url="https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=10050146&search.menuid=749&search.media=0&search.searchdate=all&search.exact=&search.include=&userDisplay=50&search.exclude=&search.onSale=1&search.option=3&search.sortBy=date&search.searchBy=0&search.searchBlockYn=0&search.includeAll=&search.query=%BE%C6%C0%CC%C6%D0%B5%E5&search.viewtype=title&search.page="+str(page_num+1)
    # search_url="https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=10050146&search.menuid=749&search.media=0&search.searchdate=all&search.defaultValue=1&search.exact=&search.include=&userDisplay=50&search.exclude=&search.onSale=1&search.option=3&search.sortBy=date&search.searchBy=0&search.searchBlockYn=0&search.includeAll=&search.query=%BE%C6%C0%CC%C6%D0%B5%E5&search.viewtype=title&search.page="+str(page_num)
    driver.get(search_url)
    driver.implicitly_wait(3)
    driver.switch_to.frame('cafe_main')
    html = driver.page_source
    dom = BeautifulSoup(html, 'html.parser')
    # dom = BeautifulSoup(urllib.request.urlopen(search_url).read().decode("cp949",'ignore'), "html.parser")
    dom1 = dom.find_all(class_='td_article')
    list = []
    cafeurl = "https://cafe.naver.com"
    for element in dom1:

        try:
            is_sell=element.find(class_="list-i-sellout").text
            if "완료" in is_sell:
                continue
        except:
            pass
        a = element.find('a')
        title = a.get_text(strip=True)
        if "아이패드" not in title:
            continue

        if any(format in title for format in passtext):
            continue # 만약 passtext의 문자열을 title이 포함하고 있다면 넘긴다!
        else:
            # print(title)
            element_url=cafeurl+a.get('href')
            # print(a.get('href'))
            list.append(element_url)
    # # ################################################################## url 가져오는 파트
    #

    save_result = []
    labels =['id','url','title','cost','text','date','img']
    # id, info_url, title, cost, text, img 순서!
    for i in range(len(list)):
        result =[]
        info_url=list[i]
        # info_url="https://cafe.naver.com/ArticleRead.nhn?clubid=10050146&page=1&menuid=749&inCafeSearch=true&searchBy=0&query=%BE%C6%C0%CC%C6%D0%B5%E5&includeAll=&exclude=&include=&exact=&searchdate=all&media=0&sortBy=date&articleid=653494415&referrerAllArticles=false"
        try:
            driver.get(info_url)
            driver.implicitly_wait(3)
            driver.switch_to.frame('cafe_main')
            html = driver.page_source
            page = BeautifulSoup(html, 'html.parser')
            inbox = page.find(class_="inbox")
            tt = page.find(id="tbody")
            img_src = tt.find(class_="image_condition").find("img").get('src')
            date = page.find(class_="tit-box").find(class_="date").text
            regex = re.compile(r"articleid=(\d+)&")
            mc = regex.search(info_url)
            # print(mc.group(1))
            # result.append(mc.group(1)) # 아이디

            id=mc.group(1)#아이디
            simple_url = "https://cafe.naver.com/joonggonara/"+mc.group(1)
            # result.append(simple_url) #url

            read_title = tt.find(class_="title").text
            read_price = tt.find(class_="cost").text
            # result.append(tt.find(class_="title").text) #타이틀
            # result.append(tt.find(class_="cost").text) #가격

            test = tt.find_all(string=True)
            index = None

            text =[]
            for i in range(len(test)):
                if "해외직구로 면세" in test[i]:
                    index = i
                    break
            test = test[index+1:]
            # print(" ".join(test).strip())
            text.append(" ".join(test).strip())
            # text.append('\n')

            read_text = " ".join(text).replace('\xa0','').replace('\xa9','').replace("\n"," ").replace("  "," ")#텍스트
            if any(format in read_text for format in passtext):
                continue # 만약 passtext의 문자열을 read_text가 포함하고 있다면 넘긴다!
            result.append(read_title)
            result.append(read_price)
            result.append(read_text)
            result.append(id)


            # date = datetime.datetime.strptime(date,'%Y.%m.%d. %H:%M')
            # print(date.date())
            result.append(date)#날짜
            result.append(img_src)#이미지 주소
            result.append(simple_url)

            save_result.append(result)
            # f.write(data)
        except:
            continue
    # df = pd.DataFrame.from_records(save_result, columns=labels)
    # df = df.applymap(lambda x: x.replace('\xa0','').replace('\xa9','').replace(',',''))
    # df.to_csv("navercafe_crawling.csv",encoding="utf-8-sig",header=False,index=False,mode='a')

    # f.close()

    # for index in range(1):
    request_data = {'navercafe_ipad': []}
    for li in save_result:
        print("##############################################################################################################")
        # li = save_result[index]
        # print(li)
        read_title=li[0]
        read_price=li[1]
        read_text=li[2]
        # print(read_title)
        # print(read_price)
        # print(read_text)
        product={}
        product=regex_function.get_model(product,read_title,read_text)
        product =regex_function.get_price(product,read_title,read_price,read_text)

        # break
        # 타이틀, 가격, 내용, 아이디, 날짜, 이미지주소, 링크
        request_data['navercafe_ipad'].append({
            'model_name': product['model_name'],
            'generation': product['generation'],
            'display': product['display'],
            'storage': product['storage'],
            'cellular': product['cellular'],
            'price': str(product['price']),
            'id': li[3],
            'date': li[4],
            'img_src': li[5],
            'link': li[6],
            'title':li[0],
            'contents':li[2]
            })
    
    # response = requests.post(API_URL + 'api/index/', data=json.dumps(request_data), headers=headers)
 