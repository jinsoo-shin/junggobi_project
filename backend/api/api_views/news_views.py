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

@api_view(['GET', 'POST'])
def news(request):
    if request.method == 'GET':
        chrome_options= webdriver.ChromeOptions() #옵션 설정하기
    #    chrome_options.add_argument('headless') #창이 안보이도록 숨기기
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.3')
        driver = webdriver.Chrome("./chromedriver.exe",chrome_options=chrome_options)

        url_list=[]
        url="https://www.google.com/search?q=%EC%95%84%EC%9D%B4%ED%8C%A8%EB%93%9C&newwindow=1&tbm=nws"
        driver.get(url)
        html = driver.page_source
        document = BeautifulSoup(html, 'html.parser')
        title = document.select(".g")
        print(len(title))
        # soup = BeautifulSoup(urllib.request.urlopen(url).read().decode('cp949', 'ignore'), "html.parser")
        # print(soup)
        title = ""
        author = ""
        category=""
        hero=""
        url=""
        request_data = {'data': []}
        request_data['data'].append({
            "title": title,
            "author": author,
            "category": category,
            "hero": hero,
            "url":url
        })
        return Response(data="",status=status.HTTP_200_OK)


    if request.method == 'POST':
    
        return Response(data="",status=status.HTTP_200_OK)

