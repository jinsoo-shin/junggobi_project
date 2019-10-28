from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
from datetime import timedelta
import time
import requests
import json

API_URL = "http://localhost:8000/api/"
headers = {'content-type': 'application/json'}

#user agent 유저인척하여 막히지 않도록!!
chrome_options= webdriver.ChromeOptions() #옵션 설정하기
# chrome_options.add_argument('headless') #창이 안보이도록 숨기기
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.3')

driver = webdriver.Chrome("../chromedriver.exe",chrome_options=chrome_options)
driver.implicitly_wait(3)
driver.get('https://m.bunjang.co.kr/')

#번개장터 접속 후, 로그인
login_number = driver.find_element_by_class_name("sc-cQFLBn")
login_number.find_element_by_tag_name("input").send_keys("01071193527")
password = driver.find_element_by_class_name("sc-gojNiO")
password.find_element_by_tag_name("input").send_keys("junggobi1014!")
btn = driver.find_element_by_class_name("sc-daURTG").click()

#아이패드 검색
search = driver.find_element_by_class_name("sc-jKJlTe")
search.find_element_by_class_name("sc-eNQAEJ").send_keys("아이패드")
search.find_element_by_class_name("sc-eNQAEJ").send_keys(Keys.RETURN)

#아이패드 리스트 찾기
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
u_list = driver.find_element_by_class_name("sc-gRnDUn").find_elements_by_tag_name("img")
url_list = []
img_url_list = []
for i in u_list:
    src_url = i.get_attribute("src")
    src = src_url.split("https://seoul-p-studio.bunjang.net/product/")
    if len(src)>=2:
        src = src[1][0:9]
        if src[8]=="_":
            src = src[0:8]
        url_list.append(src)
        img_url_list.append(src_url)
print(url_list)

#오늘 날짜 확인
today = datetime.today().strftime("%Y%m%d")


#상세페이지 웹 크롤링
cnt=0
request_data = {'product_info': []}
for data in url_list:
    url = "https://m.bunjang.co.kr/products/"+data+"?ref=검색결과&q=아이패드"
    driver.get(url)
    try:
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        sell = soup.select("#app > div.router-view > div > div.product-detail-wrapper > div:nth-child(2) > div:nth-child(1) > div.suggested-products-title")
        if len(sell)==0:
            title = soup.select("#root > div > div > div.sc-gJqsIT.hbVxbC > div.sc-kDhYZr.ikrBOB > div > div.sc-hcnlBt.jfMCiR > div > div.sc-iHhHRJ.gVVJLD > div > div.sc-gPzReC.fWxkCf > div.sc-jrIrqw.hOgugl > div.sc-hjRWVT.bbGQaP")
            price = soup.select("#root > div > div > div.sc-gJqsIT.hbVxbC > div.sc-kDhYZr.ikrBOB > div > div.sc-hcnlBt.jfMCiR > div > div.sc-iHhHRJ.gVVJLD > div > div.sc-gPzReC.fWxkCf > div.sc-jrIrqw.hOgugl > div.sc-iybRtq.eazFIt > div")
            # status = soup.select("#root > div > div > div.sc-koErNt.hoSImv > div.sc-gJqsIT.eMTckw > div > div.sc-cFlXAS.hJvCHs > div > div.sc-jRhVzh.bynJLV > div > div.sc-gPzReC.fWxkCf > div.sc-cEvuZC.jcUgmG > div.sc-dxZgTM.eVVlYD > div:nth-child(1) > div.sc-iFMziU.eMXTei")
            # exchange = soup.select("#root > div > div > div.sc-koErNt.hoSImv > div.sc-gJqsIT.eMTckw > div > div.sc-cFlXAS.hJvCHs > div > div.sc-jRhVzh.bynJLV > div > div.sc-gPzReC.fWxkCf > div.sc-cEvuZC.jcUgmG > div.sc-dxZgTM.eVVlYD > div:nth-child(2) > div.sc-iFMziU.eMXTei")
            location = soup.select("#root > div > div > div.sc-gJqsIT.hbVxbC > div.sc-kDhYZr.ikrBOB > div > div.sc-hcnlBt.jfMCiR > div > div.sc-iHhHRJ.gVVJLD > div > div.sc-gPzReC.fWxkCf > div.sc-cEvuZC.jcUgmG > div.sc-dxZgTM.eVVlYD > div:nth-child(4) > div.sc-iFMziU.cXlMvV")
            description = soup.select("#root > div > div > div.sc-gJqsIT.hbVxbC > div.sc-kDhYZr.ikrBOB > div > div.sc-lnrBVv.hvYxyl > div.sc-OxbzP.hZrvrw > div.sc-hvvHee.jlHWKG > div.sc-kcbnda.cuxerH > div.sc-dHmInP.eQnWXw > div.sc-ejGVNB.ldIAac")
            check_date = soup.select("#root > div > div > div.sc-gJqsIT.hbVxbC > div.sc-kDhYZr.ikrBOB > div > div.sc-hcnlBt.jfMCiR > div > div.sc-iHhHRJ.gVVJLD > div > div.sc-gPzReC.fWxkCf > div.sc-cEvuZC.jcUgmG > div.sc-kXeGPI.grTZPy > div > div:nth-child(3)")
            date = ""
            if len(check_date)!=0:
                check_date = check_date[0].text
                if "일 전" in check_date:
                    upload_date = check_date.replace("일 전", "")
                    upload_date*=1
                    date = datetime(today.year, today.month, today.day) - timedelta(upload_date)
                    date = date.strftime("%Y%m%d")
                else:
                    date = today
            id = data
            title = title[0].text
            price = price[0].text.replace("원","").replace(",","")
            
            # status = status[0].text
            # exchange = exchange[0].text
            location = location[0].text.replace("지역인증","")

            description = description[0].text
            size = ""
            if "매입" not in title:
                cellular = "WIFI"
                if "셀룰러" in title:
                    cellular = "셀룰러"
                elif "cellular" in title:
                    cellular = "셀룰러"
                elif "Cellular" in title:
                    cellular = "셀룰러"
                if "기가" in title:
                    index = title.find("기가")
                    size = title[(index-3):index]
                size_list = ["16","32","64","128","256","512"]
                if len(size) == 0:
                    for s_l in size_list:
                        if s_l in title:
                            size = s_l
                            break
                
                inch = ""
                generation = ""
                if "세대" in title:
                    index1 = title.find("세대")
                    generation = title[(index1-1):index1]
                inch_list =['12.9','11','10.2','10.5','9.7','7.9']
                for i_c in inch_list:
                    if i_c in title:
                        inch = i_c
                        break
                category = ""
                category_list1 = ["미니", "mini"]
                for c_g in category_list1:
                    if c_g in title:
                        category =  " 미니"
                        break
                if len(category)==0 :
                    category_list2 = ["에어", "air"]
                    for c_g in category_list2:
                        if c_g in title:
                            category = " 에어"
                            break
                if len(category)==0 :
                    category_list3 = ["프로", "pro"]
                    for c_g in category_list3:
                        if c_g in title:
                            category = " 프로"
                            break
                # print(title)
                # print(price)
                # # print(status)
                # # print(exchange)
                # print(location)
                # # print(description)
                # print(date)
                # print(generation)
                # print(category)
                # print(inch)
                # print(cellular)
                # print(size)
                # print(url)
                # print(img_url_list[cnt])
                
                request_data['product_info'].append({
                    'id' : data,
                    'category' : "태블릿",
                    'manufacturer' : "애플",
                    'model_name' : '아이패드'+category,
                    'generation' : generation+"세대",
                    'display' : inch,
                    'cellular' : cellular,
                    'storage' : size+"GB",
                    'price' : price,
                    'region' : location,
                    "date" : date,
                    'link' : url,
                    'img_src' : img_url_list[cnt],
                    'is_sell' : False,
                    'title' : title,
                    'contents' : description
                })
                print(cnt)
            #cnt 주석 예정#####################
            # if cnt==1:
            #     break
            # time.sleep(3)
            cnt+=1
        else:
            print("상품이 판매되었습니다.")
    except:
        cnt+=1
        print("제대로 처리 되지 않습니다")
        continue
response = requests.post(API_URL+"product/", data=json.dumps(request_data), headers=headers)
print(request_data)
    