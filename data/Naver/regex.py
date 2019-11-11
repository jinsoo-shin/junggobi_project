#-*- coding:utf-8 -*-


from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import urllib.request
import re

# text = "배터리*아이패드 프로 2세대 10.5인치 256gb (와이파이)팝니다. *아이패드 프로 2세대 10.5인치 256gb (와이파이)팝니다. 구매일은 2018년 8월 30일입니다. 애플 케어 먹여서 20년 8월 30일까지 리퍼 가능하고, 19년 8월 30일 (19년6월 생산)에 리퍼 한번 받아서 상태 S급입니다. 애플 펜슬은 효율 아직 좋습니다.  아이패드, 애플 펜슬 풀박스이고, 충전단자는 제가 따로사서 써서,  내부 USB, 케이블 다 새상품입니다. 리퍼기간 약 10개월 남았고, 내부 액세사리 새상품, 풀박스, +강화필름, 케이스 (펜슬 케이스, 실리콘 케이스, 하드케이스 2개) 구성 상품입니다.  가격은 700,000원 이구요 직거래는 부산대 가능합니다 안전거래도 가능합니다.  많은 연락바랍니다. 010-2사83-25팔4"

# text = "아이패드 미니5 256G 와이파이모델 그레이색상 팝니다 (미개봉) 그레이색상 1대 53만입니다  직거래 성남입니다 010 2300 3999"

# text="아이패드 프로 3세대, 12.9인치, 셀룰러, 512기가 팝니다 (상태 A++) 1,400,000원 밖에 들고나간 적도 한번도 없고 집에서도 거의 사용을 안 하고 모셔만 둔 거라  상태는 그냥 새 것과 같다고 보셔도 좋을 정도로 아주 깨끗합니다.  아이패드는 정상해지 완료해서 통신사 등록 및 확정기변 가능하세요.  리퍼기간은 2020. 7. 29까지입니다.  가격: 140만원 ※ 에눌 문의는 일절 사양합니다!! 문의주셔도 답변하지 않습니다~  거래방법: 직거래만 합니다! (※ 사정상 서울 7호선 장승배기역에서만 거래 가능해요!) 연락처: 010-3삼사8-삼54공 (문자로 주세요~) 구매시 미사용 액정필름도 같이 드립니다.  현재 부착된 필름은 랩씨 종이질감 스케치 필름입니다 제가 붙인거라 안에 있는 먼지를 제거한다고 끝부분을 한번 뗐다가 다시 붙였더니 아래 사진처럼 기포가 ㅠㅠ 사용시 불편한 점은 없는데 거슬리시면 그냥 떼고 쓰시면 될 것 같아요 그 외 따로 말씀드릴 사항 없이 상태 아주 깨끗합니다~ "
# '원$' #원으로 끝나야한다.

text = "1,000,000원"
# text = "1,000원"
# text = "1000원"
# text = "100만입니다"
text2 = "100만원입니다"
text2 = "8.9만"
#+'\d+' # \d+ : 숫자가 하나 이상이어야 함

# regex = re.compile("\d+만\w*")
# mc = regex.findall(text)
# print(mc)
try:
    regex = re.compile(r"(\d*?[,]?\d*?[,]?\d+)원\w*")
    mc = regex.search(text)
    print(mc.group(1))

    print("=>"+mc.group(1).replace(",", "")+"원")
except:
    pass

try:
    regex = re.compile(r"(\d*?[,|.]?\d*?[,|.]?\d+)만[원]*\w*")
    mc = regex.search(text2)
    print(mc.group(1))
    num = float(mc.group(1).replace(",",""))*10000
    print(num)
    print("=>" + str(round(num)) + "원")
except:
    pass

# regex = re.compile(r"(\d+)[기가|GB|gb]\w*")
# mc = regex.search(text)
# print(mc.group(1))

# regex = re.compile("\d+만\w*")
# mc = regex.findall(text)
# print(mc)


ttt = "date&articleid=653494415&referrerAllArticles=false"

regex = re.compile(r"articleid=(\d+)&")
mc=regex.search(ttt)
print(mc.group(1))