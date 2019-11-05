from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TabletSerializer, ProductSerializer, Product_Info_Serializer
from api.models import Tablet, Product, ProductInfo
import datetime
from django.db import connection, connections
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import json
headers = {'content-type': 'application/json'}
@api_view(['GET', 'POST'])
def news(request):
    if request.method == 'GET':
        chrome_options= webdriver.ChromeOptions() #옵션 설정하기
        #chrome_options.add_argument('headless') #창이 안보이도록 숨기기
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.3')
        driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)#ubuntu
        # driver = webdriver.Chrome("./chromedriver.exe",chrome_options=chrome_options)#window

        url_list=[]
        url_list.append("https://www.google.com/search?q=%EC%95%84%EC%9D%B4%ED%8C%A8%EB%93%9C&newwindow=1&tbm=nws")#아이패드
        url_list.append("https://www.google.com/search?q=%EC%95%84%EC%9D%B4%ED%8F%B0&newwindow=1&tbm=nws")#아이폰
        url_list.append("https://www.google.com/search?q=%EA%B0%A4%EB%9F%AD%EC%8B%9C%20%EB%85%B8%ED%8A%B8&newwindow=1&tbm=nws")#갤럭시 노트
        
        request_data = {'data': []}    
        for url_news in url_list:
        
            driver.get(url_news)
            html = driver.page_source
            document = BeautifulSoup(html, 'html.parser')
            cards = document.select(".g")

            title = ""
            author = ""
            category=""
            hero=""
            url=""

            for i in range(3):
                try:
                    card = cards[i].select("div")
                    try:
                        url = card[1].select("a")[0].attrs['href']     
                    except:
                        url = card[0].select("div>div")[0].select("a")[0].attrs['href']
                    if "http://www.itworld.co.kr/" in url:
                        news_page = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
                        title = news_page.select("h3")[0].text
                        title= title.replace("\r\n\t  \t","")
                        for ii in news_page.select('.node_body>img'):
                            hero = "http://itworld.co.kr"+ii.attrs['src']
                            break
                        if hero is "":
                            hero = "https://media.licdn.com/dms/image/C510BAQGI6bReiFqNbQ/company-logo_200_200/0?e=2159024400&v=beta&t=am4p3LK6gMAETjIN75BVTmcRJrpEft501Hnr1-ssEm4"    
                        author = "ITWorld Korea"
                    elif "www.bloter.net" in url:
                        news_page = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
                        title = news_page.select_one("h1").text
                        imgs = news_page.select("img")
                        author = "블로터닷넷"
                        for img in imgs:
                            try:
                                if "www.bloter.net/wp-content/uploads" in img.attrs['src']:
                                    hero = img.attrs['src']
                                    break
                            except:
                                continue
                    elif "autodaily.co.kr" in url:
                        author = "오토데일리"
                        news_page = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
                        title = news_page.select(".article-head-title")[0].text
                        imgs = news_page.select("img")
                        for img in imgs:
                            try:
                                if "/news/photo/" in img.attrs['src']:
                                    hero = "http://www.autodaily.co.kr"+img.attrs['src']
                                    break
                            except:
                                continue
                    elif "biz.chosun.com" in url:
                        author = "조선비즈"
                        news_page = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
                        title = news_page.select_one("h1").text
                        hero = news_page.select("img")[0].attrs['src']
                    elif "www.hankyung.com" in url:
                        author = "한국경제"
                        news_page = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
                        title = news_page.select_one(".title").text
                        hero = news_page.select(".articleimage>img")[0].attrs['src']
                    elif "http://www.farminsight.net/" in url:
                        author = "팜인사이트"
                        news_page = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
                        title = news_page.select(".article-head-title")[0].text
                        imgs = news_page.select("img")
                        for img in imgs:
                            try:
                                if "/news/photo/" in img.attrs['src']:
                                    hero = "http://www.farminsight.net"+img.attrs['src']
                                    break
                            except:
                                continue
                    else:
                        continue
                    request_data['data'].append({
                        "title": title,
                        "author": author,
                        "category": category,
                        "hero": hero,
                        "url":url
                    })
                    title = ""
                    author = ""
                    category=""
                    hero=""
                    url=""
                except:
                    continue
       
        return Response(request_data)


    if request.method == 'POST':
    
        return Response(data="",status=status.HTTP_200_OK)

