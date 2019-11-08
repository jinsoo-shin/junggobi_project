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

#갤럭시노트 검색
search = driver.find_element_by_class_name("sc-jKJlTe")
search.find_element_by_class_name("sc-eNQAEJ").send_keys("갤럭시노트")
search.find_element_by_class_name("sc-eNQAEJ").send_keys(Keys.RETURN)

#갤럭시노트 리스트 찾기
driver.implicitly_wait(10)
u_list = driver.find_element_by_class_name("sc-gRnDUn").find_elements_by_tag_name("img")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
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
today = datetime.today()

#상세페이지 웹 크롤링
cnt=0
request_data = {'product_info': []}
for data in url_list:
    url = "https://m.bunjang.co.kr/products/"+data+"?ref=검색결과&q=갤럭시노트"
    driver.get(url)

    try:
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        sell = soup.select("#app > div.router-view > div > div.product-detail-wrapper > div:nth-child(2) > div:nth-child(1) > div.suggested-products-title")
        if len(sell)==0:
            title = soup.select("#root > div > div > div.sc-hkbPbT.dVsAzx > div.sc-jRhVzh.fVCcFK > div > div.sc-hvvHee.hWetCH > div > div.sc-dXfzlN.eiTWPc > div > div.sc-gPzReC.fWxkCf > div.sc-jrIrqw.hOgugl > div.sc-hjRWVT.bbGQaP")
            price = soup.select("#root > div > div > div.sc-hkbPbT.dVsAzx > div.sc-jRhVzh.fVCcFK > div > div.sc-hvvHee.hWetCH > div > div.sc-dXfzlN.eiTWPc > div > div.sc-gPzReC.fWxkCf > div.sc-jrIrqw.hOgugl > div.sc-iybRtq.eazFIt > div")
            # status = soup.select("#root > div > div > div.sc-koErNt.hoSImv > div.sc-gJqsIT.eMTckw > div > div.sc-cFlXAS.hJvCHs > div > div.sc-jRhVzh.bynJLV > div > div.sc-gPzReC.fWxkCf > div.sc-cEvuZC.jcUgmG > div.sc-dxZgTM.eVVlYD > div:nth-child(1) > div.sc-iFMziU.eMXTei")
            # exchange = soup.select("#root > div > div > div.sc-koErNt.hoSImv > div.sc-gJqsIT.eMTckw > div > div.sc-cFlXAS.hJvCHs > div > div.sc-jRhVzh.bynJLV > div > div.sc-gPzReC.fWxkCf > div.sc-cEvuZC.jcUgmG > div.sc-dxZgTM.eVVlYD > div:nth-child(2) > div.sc-iFMziU.eMXTei")
            location = soup.select("#root > div > div > div.sc-gJqsIT.hbVxbC > div.sc-kDhYZr.ikrBOB > div > div.sc-hcnlBt.jfMCiR > div > div.sc-iHhHRJ.gVVJLD > div > div.sc-gPzReC.fWxkCf > div.sc-cEvuZC.jcUgmG > div.sc-dxZgTM.eVVlYD > div:nth-child(4) > div.sc-iFMziU.cXlMvV")
            description = soup.select("#root > div > div > div.sc-hkbPbT.dVsAzx > div.sc-jRhVzh.fVCcFK > div > div.sc-jHZirH.UZhFH > div.sc-iIHjhz.jGgLdl > div.sc-dBAPYN.etrmdO > div.sc-kcbnda.cuxerH > div.sc-dHmInP.eQnWXw > div.sc-ejGVNB.ldIAac")
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
            description = description[0].text
            price = price[0].text.replace(",","")
            

            if len(location)!=0:
                    location = location[0].text
            start_check = True

            title_list = ["삽니다", "급매", "매입", "주의사항"]
            for t_l in title_list:
                if t_l in title:
                    start_check = False
                    break
                if t_l in description:
                    start_check = False
                    break
            if "노트" not in title:
                start_check = False
            if start_check == True:
                size = ""
                category = ""
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
                ten_plus = ["+", "플러스", "plus"]
                for i in range(1,12,1):
                    if str(i) in title:
                        category = str(i)
                        if i >= 8:
                            for t_p in ten_plus:
                                if t_p in title:
                                    category += " 플러스"

                
                # print(title)
                # print(size)
                # print(description)
                # print(location)
                # print(category)
                # print(price)

                request_data['product_info'].append({
                    'id' : data,
                    'category' : "모바일",
                    'manufacturer' : "삼성전자",
                    'model_name' : '갤럭시 노트'+category,
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
            cnt+=1
        else:
            print("상품이 판매되었습니다.")
    except:
        print("제대로 처리 되지 않습니다")
        cnt+=1
        continue
response = requests.post(API_URL+"product/", data=json.dumps(request_data), headers=headers)
print(request_data)
    
