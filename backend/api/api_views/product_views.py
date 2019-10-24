from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TabletSerializer, ProductSerializer, Product_Info_Serializer
from api.models import Tablet, Product, ProductInfo
import datetime
from django.db import connection, connections
@api_view(['GET','POST'])
def information(request):
    if request.method=='GET':
        product_info = ProductInfo.objects.all()
        serializer = Product_Info_Serializer(product_info, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        for cur_data in product_info:
            id = cur_data.get("id", None)
            category = cur_data.get("category", None)
            manufacturer = cur_data.get("manufacturer",None)
            model_name = cur_data.get("model_name",None)
            print(model_name)
            generation = cur_data.get("generation",None)
            if len(generation)== len("세대"):
                generation = None
            display = cur_data.get("display",None)
            if len(display)==0:
                display = None
            cellular = cur_data.get("cellular",None)
            storage = cur_data.get("storage",None)
            price = cur_data.get("price",None)
            region = cur_data.get("region",None)
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
                        display=display,cellular=cellular,storage=storage,price=price,region=region, date=date,link=link,img_src=img_src,is_sell=is_sell,title=title,contents=contents).save()

            # pass
        return Response(status=status.HTTP_200_OK)
