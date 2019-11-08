#-*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import urllib.request
import re
import csv
import pandas as pd




def get_model(read_title,read_text):
    model = "" # 아이패드2 아이패드미니 아이패드프로, 아이패드에어
    gen = "" # ?세대
    inch = "" #몇인치인가?

#인치를 타이틀에서 삭제
    inch_list =['12.9','11','10.2','10.5','9.7','7.9']
    inch = "".join([s for s in inch_list if s in read_title])
    read_title = read_title.replace(inch,"")
    # print("/////////인치 제거한 타이틀",read_title)


##용량을 타이틀에서 삭제
    memory = get_memory(read_title,"") #용량을 가져옴
    if memory:
        memory_list = ['GB','기가']
        for i in range(len(memory_list)):
            memory_list[i]=memory+memory_list[i]
        delete_text = "".join([s for s in memory_list if s in read_title])
        read_title = read_title.replace(delete_text, "")
        # print("/////////용량제거한 타이틀",read_title)
        memory=memory+"GB"
    else:
        if "1TB" in read_title:
            memory = '1TB'
            read_title = read_title.replace("1TB", "")
            # print("//////용량제거한 타이틀", read_title)

##큰모델 가져오기
    if "미니" in read_title:
        model = "아이패드 미니"
        try:
            regex = re.compile(r"[미니|미니 ]?(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    elif "에어" in read_title:
        model = "아이패드 에어"
        try:
            regex = re.compile(r"[에어|에어 ]?(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    elif "프로" in read_title:
        model = "아이패드 프로"
        try:
            regex = re.compile(r"[프로|프로 ]?(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    elif "PRO" in read_title:
        model = "아이패드 프로"
        try:
            regex = re.compile(r"[PRO|PRO ]?(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    else:
        model = "아이패드"
        try:
            regex = re.compile(r"[미니|미니 ]?(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass

    try:
        regex = re.compile(r"(\d)세대")
        mc = regex.search(read_title)
        gen=mc.group(1)
    except:
        pass


    cellular=None
    boolean_cellular = get_cellular(read_title,read_text)
    if boolean_cellular:
        cellular = "셀룰러"
    else:
        cellular = "WIFI"

    if gen is not "":
        gen = gen+"세대"
    print("모델:",model," /세대:", gen," /인치:",inch,"/용량:",memory,"/LTE:",cellular)
    request_data=[]
    request_data.append(model)
    request_data.append(gen)
    request_data.append(inch)
    request_data.append(memory)
    request_data.append(cellular)
    result = " ".join(request_data).replace("  "," ")
    # print(result)
    # return model


def get_memory(read_title,read_text):
    memory = ""
    try:
        regex = re.compile(r"(\d+)[기가|GB|gb|g]\w*")
        mc = regex.search(read_title)
        # print(mc.group(1))
        memory=mc.group(1)
    except:
        pass
    if memory is "":
        try:
            regex = re.compile(r"(\d+)[기가|GB|G]\w*")
            mc = regex.search(read_text)
            print(mc.group(1))
            memory = mc.group(1)
        except:
            pass
    return memory

def get_cellular(read_title,read_text):


    is_cellular = False
    is_wifi = False
    cellurlar_list= ['셀룰러','LTE','셀롤러']
    if any(format in read_title for format in cellurlar_list):
        is_cellular=True
    else:
        if any(format in read_text for format in cellurlar_list):
            is_cellular = True

    wifi_list = ['WIFI', '와이파이','WI-FI']
    if any(format in read_title for format in wifi_list):
        is_wifi = True
    else:
        if any(format in read_text for format in wifi_list):
            is_wifi = True

    if is_cellular:
        return True
    else:
        return False


def get_price(read_title,read_price,read_text):
    try:
        regex = re.compile(r"(\d*?[,]?\d*?[,]?\d+)원\w*")
        mc = regex.search(read_line)
        print(mc.group(1))
        print("=>"+mc.group(1).replace(",", "")+"원")
    except:
        pass

    try:
        regex = re.compile(r"(\d*?[,|.]?\d*?[,|.]?\d+)만[원]*\w*")
        mc = regex.search(read_line)
        print(mc.group(1))
        num = float(mc.group(1).replace(",",""))*10000
        print(num)
        print("=>" + str(round(num)) + "원")
    except:
        pass

if __name__ == '__main__':
    with open('navercafe_crawling.csv','r', encoding='utf-8-sig') as read_data:
        read_data = list(read_data)
        for i in range(len(read_data)) :
        # for i in range(10) :
            print("#############################################")
            read_line = read_data[i].split(',')
            read_title = read_line[2].upper()
            read_price = read_line[3]
            read_text = read_line[4].upper()
            print("title",read_title)
            print("price",read_price)
            print("text",read_text)

            # print("##############")
            # print("용량 몇기가일까? ",get_memory(read_line))
            # print("셀룰러 모델인가? ",get_cellular(read_line))

            # get_model(read_title,read_text)
            get_price(read_title,read_price,read_text)