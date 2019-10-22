#-*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import urllib.request
import re
import csv
import pandas as pd
from collections import Counter



def get_model(request_data,read_title,read_text):
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
        memory_list = ['GB','기가','G']
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
            regex = re.compile(r"(?<=[미니|미니 ])(\d)")
            # regex = re.compile(r"[미니|미니 ]?(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    elif "에어" in read_title:
        model = "아이패드 에어"
        try:
            regex = re.compile(r"(?<=[에어|에어 ])(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    elif "프로" in read_title:
        model = "아이패드 프로"
        try:
            regex = re.compile(r"(?<=[프로|프로 ])(\d)")
            # regex = re.compile(r"[프로|프로 ]?(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    elif "PRO" in read_title:
        model = "아이패드 프로"
        try:
            regex = re.compile(r"(?<=[PRO|PRO ])(\d)")
            # regex = re.compile(r"[PRO|PRO ]?(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    else:
        model = "아이패드"
        try:
            # regex = re.compile(r"[미니|미니 ]?(\d)")
            regex = re.compile(r"(?<=[아이패드|아이패드 ])(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    if gen is "":
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

    if model is "":
        pass
    if gen is "":
        pass
    if inch is "":
        pass
    if memory is "":
        pass
    if cellular is "":
        pass
    request_data['model_name']=model
    request_data['generation']=gen
    request_data['display']=inch
    request_data['memory']=memory
    request_data['cellular']=cellular

    return request_data
    # result = " ".join(request_data).replace("  "," ")
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

    if memory is "":
        memory_list =['16','32','64','128','256','512']
        memory = "".join([s for s in memory_list if s in read_title])

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

def get_price_from_text(price_list,text):
    try:
        regex = re.compile(r"(\d*?,?\d*?,?[^.]\d+)원\w*")
        mc = regex.findall(text)
        for m in mc:
            num = int(m.replace(",", ""))
            if num<=10000:
                continue
            price_list.append(int(num))
            # print(1,num)
    except:
        pass
    # try:
    #     regex = re.compile(r"(\d*?,?\d*?,?[^.]\d+)[\s|\S]*?만[원]?\w*")
    #     mc = regex.findall(text)
    #     for m in mc:
    #         num = int(m.replace(",", ""))*10000
    #         price_list.append(num)
    #         print(2, num)
    # except:
    #     pass
    try:
        regex = re.compile("(\d+)(?=만)")
        mc = regex.findall(text)
        for m in mc:
            num = int(m.replace(",", "")) * 10000
            if num<=10000:
                continue
            price_list.append(num)
            # print(3, num)
    except:
        pass
    try:
        regex = re.compile(r"(\d+[.]\d)만[원]?\w*")
        mc = regex.findall(text)
        for m in mc:
            num = int(m.replace(".", ""))*1000
            if num<=10000:
                continue
            price_list.append(num)
            # print(4, num)
    except:
        pass
    try:
        regex = re.compile(r"(\d+.000)[원]?\w*")
        mc = regex.findall(text)
        for m in mc:
            num = int(m.replace(".", ""))
            if num<=10000:
                continue
                # print(5,num)
            price_list.append(num)
    except:
        pass

    try:
        # regex = re.compile("(\d+)\s(?=만)")
        regex = re.compile("(\d+)[' '](?=만)")
        mc = regex.findall(text)
        for m in mc:
            num = int(m)*10000
            price_list.append(num)
    except:
        pass
    return price_list



def get_price(request_data,read_title,read_price,read_text):
    price_list=[]
    print("########################")
    print(read_title)
    print(read_price)
    print(read_text)
    get_price_from_text(price_list,read_title)
    get_price_from_text(price_list,read_price)
    get_price_from_text(price_list,read_text)
    # print(price_list)
    ## 여기서 1순위는 가장 많은것, 2순위 제일 비싼것
    count=Counter(price_list).most_common(2)
    # sorted_C_union = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    # print(sorted_C_union)
    count = sorted(count,key=lambda x:(-x[1],-x[0]))
    # print(count)
    # print(count[0][0])
    
    most_price = 0
    try :
        most_price = count[0][0]
    except:
        pass

    in_price=0
    try:
        regex = re.compile(r"(\d*?,?\d*?,?[^.]\d+)원\w*")
        mc = regex.findall(read_price)
        for m in mc:
            num = m.replace(",", "")
            if num<=10000:
                continue
            price_list.append(int(num))
            # print(1,num)
    except:
        pass
    # print("가격",most_price if most_price>=in_price else in_price)
    request_data["price"]=most_price if most_price>=in_price else in_price
    return request_data

# if __name__ == '__main__':
#     with open('navercafe_crawling.csv','r', encoding='utf-8-sig') as read_data:
#         read_data = list(read_data)
#         for i in range(len(read_data)) :
#         # for i in range(5) :
#             print("#############################################")
#             read_line = read_data[i].split(',')
#             read_title = read_line[2].upper()
#             read_price = read_line[3]
#             read_text = read_line[4].upper()
#             print("title",read_title)
#             print("price",read_price)
#             print("text",read_text)
#             request_data={} #딕셔너리 형식
#             request_data=get_model(request_data,read_title,read_text)
#             request_data =get_price(request_data,read_title,read_price,read_text)
#             print(request_data)
