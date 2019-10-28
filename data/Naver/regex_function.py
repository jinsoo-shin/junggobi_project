#-*- coding:utf-8 -*-
import requests
import time
import urllib.request
import re
import csv
import pandas as pd
from collections import Counter



def get_ipad_model(request_data,read_title,read_text):
    model = "" # 아이패드2 아이패드미니 아이패드프로, 아이패드에어
    gen = "" # ?세대
    inch = "" #몇인치인가?
    read_title=read_title.upper()
    read_text=read_text.upper()
    #인치를 타이틀에서 삭제
    inch_list =['12.9','11','10.2','10.5','9.7','7.9']
    inch = "".join([s for s in inch_list if s in read_title])
    read_title = read_title.replace(inch,"")


    ##용량을 타이틀에서 삭제
    storage = get_storage(read_title,read_text) #용량을 가져옴
    if storage:
        storage_list = ['GB','기가','G']
        for i in range(len(storage_list)):
            storage_list[i]=storage+storage_list[i]
        delete_text = "".join([s for s in storage_list if s in read_title])
        read_title = read_title.replace(delete_text, "")
        storage=storage+"GB"
    else:
        if "1TB" in read_title:
            storage = '1TB'
            read_title = read_title.replace("1TB", "")

    ##큰모델 가져오기
    if "미니" in read_title:
        model = "아이패드 미니"
        try:
            regex = re.compile(r"(?<=[미니|미니 ])(\d)")
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
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    elif "PRO" in read_title:
        model = "아이패드 프로"
        try:
            regex = re.compile(r"(?<=[PRO|PRO ])(\d)")
            mc = regex.search(read_title)
            gen = mc.group(1)
        except:
            pass
    else:
        model = "아이패드"
        try:
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
    # print("모델:",model," /세대:", gen," /인치:",inch,"/용량:",storage,"/LTE:",cellular)

    if model is "":
        pass
    if gen is "":
        pass
    if inch is "":
        pass
    if storage is "":
        pass
    if cellular is "":
        pass
    request_data['model_name']=model
    request_data['generation']=gen
    request_data['display']=inch
    request_data['storage']=storage
    request_data['cellular']=cellular

    return request_data

def get_storage(read_title,read_text):
    storage = ""
    try:
        regex = re.compile(r"(\d+)[기가|GB|gb|g]")
        mc = regex.search(read_title)
        storage=mc.group(1)
    except:
        pass

    if storage is "":
        storage_list =['16','32','64','128','256','512']
        storage = "".join([s for s in storage_list if s in read_title])

    if storage is "":
        try:
            regex = re.compile(r"(\d+)[기가|GB|G]")
            mc = regex.search(read_text)
            # print(mc.group(1))
            storage = mc.group(1)
        except:
            pass

    return storage

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
    # print("########################")
    # print(read_title)
    # print(read_price)
    # print(read_text)
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



def get_iphone_model(request_data,read_title,read_text):
    model = "" 
    read_title=read_title.upper()
    read_text=read_text.upper()
    model_list=['아이폰'] # 뒤에 붙여서 모델명을 join할 예정
    detail_model_list=[] # 프로, MAX 플러스

    ##용량을 타이틀에서 삭제
    storage = get_storage(read_title,read_text) #용량을 가져옴
    if storage:
        storage_list = ['GB','기가','G']
        for i in range(len(storage_list)):
            storage_list[i]=storage+storage_list[i]
        delete_text = "".join([s for s in storage_list if s in read_title])
        read_title = read_title.replace(delete_text, "")
        storage=storage+"GB"

    print(read_title)

    ##큰모델 가져오기
    if "플러스" in read_title:
        detail_model_list.append("플러스")
        read_title =read_title.replace("플러스","").replace("+","")
    elif "+" in read_title:
        detail_model_list.append("플러스")
        read_title =read_title.replace("플러스","").replace("+","")

    if "프로" in read_title:
        detail_model_list.append("프로")
        read_title =read_title.replace("PRO","").replace("프로","")
    elif "PRO" in read_title:
        detail_model_list.append("프로")
        read_title =read_title.replace("PRO","").replace("프로","")

    if "맥스" in read_title:
        detail_model_list.append("MAX")
        read_title =read_title.replace("맥스", "").replace("MAX", "")
    elif "MAX" in read_title:
        detail_model_list.append("MAX")
        read_title=read_title.replace("맥스", "").replace("MAX", "")

    try:
        regex = re.compile("아이폰\s?(\w+)")
        mc = regex.search(read_title)
        model_gen = mc.group(1)
        model_list.append(model_gen)
        model = " ".join(model_list)
    except:
        pass
    if len(detail_model_list) is not 0:
        detail_model = " ".join(detail_model_list)
        model = model +" "+ detail_model


    if model is "":
        model = None
    if storage is "":
        storage = None

    request_data['model_name']=model
    request_data['storage']=storage

    return request_data

def get_galaxymobile_model(request_data,read_title,read_text):
    model = ""
    read_title=read_title.upper()
    read_text=read_text.upper()
    model_list=['갤럭시'] # 뒤에 붙여서 모델명을 join할 예정
    detail_model_list=[] #

    ##용량을 타이틀에서 삭제
    storage = get_storage(read_title,read_text) #용량을 가져옴
    if storage:
        storage_list = ['GB','기가','G']
        for i in range(len(storage_list)):
            storage_list[i]=storage+storage_list[i]
        delete_text = "".join([s for s in storage_list if s in read_title])
        read_title = read_title.replace(delete_text, "")
        storage=storage+"GB"

    # print(read_title)

    ##큰모델 가져오기
    if "(+" in read_title:
        read_title = read_title.replace("(+", "")

    if "엣지" in read_title:
    detail_model_list.append("엣지")
    read_title =read_title.replace("엣지", "")

    if "+" in read_title:
        detail_model_list.append("플러스")
        read_title =read_title.replace("플러스","").replace("+","")
    elif "플러스" in read_title:
        detail_model_list.append("플러스")
        read_title =read_title.replace("플러스","").replace("+","")

    if "프로" in read_title:
        detail_model_list.append("프로")
        read_title =read_title.replace("PRO","").replace("프로","")
    elif "PRO" in read_title:
        detail_model_list.append("프로")
        read_title =read_title.replace("PRO","").replace("프로","")

    if "스타" in read_title:
        detail_model_list.append("스타")
        read_title =read_title.replace("스타", "")
    try:
        regex = re.compile("갤럭시\s?(\w+)")
        mc = regex.search(read_title)
        model_gen = mc.group(1)
        model_list.append(model_gen)
        model = " ".join(model_list)
    except:
        pass
    try:
        regex = re.compile("(201\d)")
        mc = regex.search(read_title)
        year = mc.group(1)
        # print(year)
        detail_model_list.append(year)
    except:
        pass

    if len(detail_model_list) is not 0:
        detail_model = " ".join(detail_model_list)
        model = model +" "+ detail_model
    if "7FE" in model:
        model = model.replace("7FE","FE")

    # print("모델",model)
    if model is "":
        model = None
    if storage is "":
        storage = None

    request_data['model_name']=model
    request_data['storage']=storage

    return request_data

#
# if __name__ == '__main__':
#     # detail_model_list=[]
#     product = {}
#     read_title = "삼성 갤럭시노트9 정상해지공기계 판매합니다 / 영등"
#     get_galaxymobile_model(product,read_title,"")
    # try:
    #     regex = re.compile("(201\d)")
    #     mc = regex.search(read_title)
    #     model_gen = mc.group(1)
    #     print(model_gen)
    # except:
    #     pass
    # if "+" in read_title:
    #     detail_model_list.append("플러스")
    #     read_title =read_title.replace("플러스", "")
    # elif "플러스" in read_title:
    #     detail_model_list.append("플러스")
    #     read_title=read_title.replace("플러스", "")
    # print(detail_model_list)
#     product={}

#     read_title = "아이폰7 레드 128기가"
#     read_price ="22,222원"
#     read_text="풀 박스 입니다. 공기계 상태 입니다. 찍힘, 스크레치 없습니다. 판매금액 26만원 % 8구6구 7lo7 연락주세요."
#     product= get_iphone_model(product,read_title,read_text)
#     product =get_price(product,read_title,read_price,read_text)
#     print(product)


# 아이폰7 레드 128기가
# 풀 박스 입니다. 공기계 상태 입니다. 찍힘, 스크레치 없습니다. 판매금액 26만원 % 8구6구 7lo7 연락주세요.
# 22,222원
# ##################################################
# 아이폰xs 스그 풀박스  리퍼 남음
# 아이폰xs 풀박스 판매합니다 64기가 충전기 케이블 이어폰 다 있습니다 케이블은 사용도 안했습니다. 배터리 성능 100프로 입니다 리퍼기간은 2020년 3월10일 까지입니다.
# 서울 직거래 상태는 사진처럼 좋습니다 왼쪽 아래에 작은 기스 있습니다! 나머지는 상태 S급입니다 서브 폰으로 집에서 사용해서 좋습니다!  강화유리 부착중입니다!      
# 700,000원
# ##################################################
# 아이폰7 플러스 32기가 매트블랙
# [10-247] 아이폰7 플러스 32기가 매트블랙 상태 좋습니다 리퍼 만료입니다 기기단품입니다 배터리89% 25%선택약정가능합니다. 통신사 상관없시 사용한기기입니다 유심만꽂 
# 으면 바로사용가능합니다 기능검수이상없습니다 역삼역2번출구 직거래가능합니다 댓글이나 쪽지 확인못해요 010-9191-2541 연락주세요
# 290,000원
# ##################################################
# 아이폰XS Max 골드256gb 부산
# 아이폰XS맥스골드256gb지난해11월구입 사용잘했구요해지했습니다25%할인되구요 리퍼기간은11월까지입니다전화용으로사용해서 배터리좋습니다사진테두리작게한군데말고는 매
# 우깨끗해요폰만있고쓰던케이스드릴께요
# 800,000원
# ##################################################
# 아이폰XR 128기가 레드
# [10-244] 아이폰XR 128기가 레드 상태 좋습니다 리퍼 1월2일까지 입니다 기기단품입니다 배터리96% 25%선택약정불가능합니다. 통신사 상관없시 사용한기기입니다 유심만꽂 
# 으면 바로사용가능합니다 기능검수이상없습니다 역삼역2번출구 직거래가능합니다 댓글이나 쪽지 확인못해요 010-9191-2541 연락주세요
# 580,000원
# ##################################################
# 아이폰8 64기가 골드
# [10-243] 아이폰8 64기가 골드 상태 좋습니다 백점하나있어요 리퍼 만료입니다 기기단품입니다 배터리84% 25%선택약정가능합니다. 통신사 상관없시 사용한기기입니다 유심 
# 만꽂으면 바로사용가능합니다 기능검수이상없습니다 역삼역2번출구 직거래가능합니다 댓글이나 쪽지 확인못해요 010-9191-2541 연락주세요
# 300,000원



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
