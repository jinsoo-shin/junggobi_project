from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
from datetime import timedelta
import time
import requests
import json

API_URL = "http://52.78.203.0:8000/api/"
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

#아이폰 검색
search = driver.find_element_by_class_name("sc-jKJlTe")
search.find_element_by_class_name("sc-eNQAEJ").send_keys("아이폰")
search.find_element_by_class_name("sc-eNQAEJ").send_keys(Keys.RETURN)

#아이폰 리스트 찾기
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
u_list = driver.find_element_by_class_name("sc-gRnDUn").find_elements_by_tag_name("img")
url_list = []
img_url_list = []
for i in u_list:
    src_url = i.get_attribute("src")
    # print(src_url)
    src = src_url.split("https://seoul-p-studio.bunjang.net/product/")
    if len(src)>=2:
        src = src[1][0:9]
        if src[8]=="_":
            src = src[0:8]
        url_list.append(src)
        img_url_list.append(src_url)
print(url_list)
#오늘 날짜 확인
today = datetime.today()

#상세페이지 웹 크롤링
cnt=0
request_data = {'product_info': []}
for data in url_list:
    url = "https://m.bunjang.co.kr/products/"+data+"?ref=검색결과&q=아이폰"
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
            location = soup.select("#root > div > div > div.sc-gJqsIT.hbVxbC > div.sc-kDhYZr.ikrBOB > div > div.sc-hcnlBt.jfMCiR > div > div.sc-iHhHRJ.gVVJLD > div > div.sc-gPzReC.fWxkCf > div.sc-cEvuZC.jcUgmG > div.sc-dxZgTM.eVVlYD > div:nth-child(4) > div.sc-iFMziU.cpTpen")
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
                    date = today.strftime("%Y%m%d")
            title = title[0].text
            price = price[0].text.replace("원","").replace(",","")
            
            # status = status[0].text
            # exchange = exchange[0].text
            # print(location[0].text)
            if len(location)!=0:
                location = location[0].text
            description = description[0].text
            size = ""
            title_list = ["매입", "주의사항"]
            start_check = True
            for t_l in title_list:
                if t_l in title:
                    start_check = False
                    break
                if t_l in description:
                    start_check = False
                    break

            if start_check == True:
                size_list = ["16","32","64","128","256","512"]
                if "기가" in title:
                    for s_l in size_list:
                        if s_l in title:
                            size = s_l
                            break
                if len(size) == 0:
                    for s_l in size_list:
                        if s_l in title:
                            size = s_l
                            break
                generation = ""
                if "세대" in title:
                    index1 = title.find("세대")
                    generation = title[(index1-1):index1]
                category = ""
                s_list = ["6S", "6s", "6"]
                for s_l in s_list:
                    if s_l in title:
                        if s_l == "6s":
                            category="6S"
                        else:
                            category=" "+s_l
                        category_list1 = ["플러스", "plus", "+"]
                        for c_l in category_list1:
                            if c_l in title:
                                category  +=" 플러스"
                                break
                if len(category)==0:
                    s_list1 = ["7S", "7s", "7"]
                    for s_l in s_list1:
                        if s_l in title:
                            if s_l=="7s":
                                category = " 7S"
                            else:
                                category=" "+s_l
                            category_list1 = ["플러스", "plus", "+"]
                            for c_l in category_list1:
                                if c_l in title:
                                    category +=" 플러스"
                                    break
                if len(category)==0:
                    s_list1 = ["8S", "8s", "8"]
                    for s_l in s_list1:
                        if s_l in title:
                            if s_l=="8s":
                                category = " 8S"
                            else:
                                category=" "+s_l
                            category_list1 = ["플러스", "plus", "+"]
                            for c_l in category_list1:
                                if c_l in title:
                                    category +=" 플러스"
                                    break
                if len(category)==0:
                    s_list1 = ["X", "XR", "xr", "x", "xs", "XS", "xs max", "XS 맥스", "XS MAX", "xs 맥스"]
                    for s_l in s_list1:
                        if s_l in title:
                            if s_l=="x":
                                category = " X"
                            elif s_l == "xr":
                                category = " XR"
                            elif s_l == "xs":
                                category = " XS"
                            elif s_l == "xs max":
                                category = " XS MAX"
                            elif s_l == "XS 맥스":
                                category = " XS MAX"
                            elif s_l == "xs 맥스":
                                category = " XS MAX"                            
                            else:
                                category=" "+s_l
                # print(cnt)
                # print(title)
                # print(price)
                # print(status)
                # print(exchange)
                print(location)
                # print(description)
                # print(date)
                # print(category)
                # print(url)
                # print(img_url_list[cnt])
                request_data['product_info'].append({
                    'id' : data,
                    'category' : "모바일",
                    'manufacturer' : "애플",
                    'model_name' : '아이폰'+category,
                    'generation' : "세대",
                    'display' : "",
                    'cellular' : "",
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
            #cnt 주석 예정#####################
            # if cnt==1:
            #     break
            # time.sleep(3)

            cnt+=1
        else:
            print("상품이 판매되었습니다.")
    except:
        print("제대로 처리 되지 않습니다")
        cnt+=1
        continue
response = requests.post(API_URL+"product/", data=json.dumps(request_data), headers=headers)
print(request_data)
    