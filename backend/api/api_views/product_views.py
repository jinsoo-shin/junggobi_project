from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TabletSerializer, ProductSerializer, Product_Info_Serializer
from api.models import Tablet, Product, ProductInfo
import datetime
from django.db import connection, connections
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from api.search import bulk_indexing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import requests
import json

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def information(request):
    if request.method=='GET':
        search_word = request.query_params.get('search')

        if not search_word:
            product_info = ProductInfo.objects.all()
            
            check = request.GET.get('is_sell',None)
            bungae = request.GET.get('link', None)
            id = request.GET.get('id',None)
            if check:
                product_info = product_info.filter(is_sell__iexact=check)
            if id:
                product_info = product_info.filter(id__iexact=id)
            if bungae:
                product_info = product_info.filter(link__icontains=bungae)

            serializer = Product_Info_Serializer(product_info, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
            # return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})

        es = Elasticsearch()
        docs = es.search(index='productinfo-index',
                         # doc_type='navercafe_index',
                         body={
                             "query": {
                                 "multi_match": {
                                     "query": search_word,
                                     "fields": ["title", "contents", "region"]
                                 }
                             }
                         })

        data_list = docs['hits']
        print(data_list)
        return Response(data_list)

    elif request.method == 'POST':
        product = request.data.get('product', None)
        tablet = request.data.get('tablet', None)
        navercafe_ipad = request.data.get('navercafe_ipad',None)
        product_info = request.data.get('product_info',None)
        if product_info:
            for cur_data in product_info:
                id = cur_data.get("id", None)
                category = cur_data.get("category", None)
                manufacturer = cur_data.get("manufacturer",None)
                model_name = cur_data.get("model_name",None)
                print(model_name)
                generation = cur_data.get("generation",None)
                if len(generation)==len("세대"):
                    generation = None
                display = cur_data.get("display",None)
                if len(display)==0:
                    display = None
                cellular = cur_data.get("cellular",None)
                if len(cellular)==0:
                    cellular = None
                storage = cur_data.get("storage",None)
                if len(storage)==len("GB"):
                    storage = None
                price = cur_data.get("price",None)
                region = cur_data.get("region",None)
                if len(region)==0:
                    region = None
                date = cur_data.get("date",None)
                date = datetime.datetime.strptime(date,'%Y%m%d')
                date= date.date()
                link = cur_data.get("link",None)
                img_src = cur_data.get("img_src",None)
                is_sell = False
                title = cur_data.get("title",None)
                contents = cur_data.get("contents",None)
                # if display is "":
                #     display=None
                # 타이틀, 가격, 내용, 아이디, 날짜, 이미지주소, 링크
                ProductInfo(id=id,category=category, manufacturer=manufacturer, model_name=model_name, generation=generation,
                            display=display,cellular=cellular,storage=storage,price=price,region=region, date=date,link=link,img_src=img_src
                            ,is_sell=is_sell,title=title,contents=contents).save()
        if product:
            for cur_product in product:
                id = cur_product.get("id",None)
                category = cur_product.get("category",None)
                manufacturer = cur_product.get("manufacturer",None)
                model_name = cur_product.get("model_name",None)
                generation = cur_product.get("generation",None)
                display = cur_product.get("display",None)
                release_date = cur_product.get("release_date",None)
                Product(id=id, category=category, manufacturer=manufacturer, model_name=model_name, generation=generation ,
                        display=display,release_date=release_date).save()
        if tablet:
            for cur_tablet in tablet:
                product_id = cur_tablet.get("product_id", None)
                key_name = cur_tablet.get("key_name",None)
                cellular = cur_tablet.get("cellular",None)
                storage = cur_tablet.get("storage",None)
                price = cur_tablet.get("price",None)
                query = cur_tablet.get("query",None)
                Tablet(product_id=product_id,key_name=key_name, cellular=cellular, storage=storage, price=price,query=query).save()
        if navercafe_ipad:
            for cur_data in navercafe_ipad:
                id = cur_data.get("id", None)
                category = cur_data.get("category",None)
                manufacturer = cur_data.get("manufacturer",None)
                model_name = cur_data.get("model_name",None)
                generation = cur_data.get("generation",None)
                display = cur_data.get("display",None)
                cellular = cur_data.get("cellular",None)
                storage = cur_data.get("storage",None)
                price = cur_data.get("price",None)
                region = cur_data.get("region",None)
                date = cur_data.get("date",None)
                date =datetime.datetime.strptime(date,'%Y.%m.%d. %H:%M') #2019.10.24 11:05
                date= date.date()
                link = cur_data.get("link",None)
                img_src = cur_data.get("img_src",None)
                title = cur_data.get("title",None)
                contents = cur_data.get("contents",None)
                is_sell = cur_data.get("is_sell",False)

                if generation is "":
                    generation=None
                if display is "":
                    display=None
                if storage is "":
                    storage=None
                ProductInfo(id=id,category=category, manufacturer=manufacturer, model_name=model_name, generation=generation,
                          display=display,cellular=cellular,storage=storage,price=price,date=date,link=link,img_src=img_src,
                            is_sell=is_sell,title=title,contents=contents).save()
            #elasticsearch index 추가추가
            bulk_indexing()

        return Response(status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        product_info = ProductInfo.objects.get(id=id)
        serializer = Product_Info_Serializer(product_info, data=request.DATA)
        if serializer.is_valid():
            ProductInfo(id=id,category=category, manufacturer=manufacturer, model_name=model_name, generation=generation,
                          display=display,cellular=cellular,storage=storage,price=price,date=date,link=link,img_src=img_src,
                            is_sell=1,title=title,contents=contents).save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


if __name__ == "__main__":
    information()