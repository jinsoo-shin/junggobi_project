from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TabletSerializer, ProductSerializer,NavercafeSerializer
from api.models import Tablet,Product,Navercafe
import datetime
from django.db import connection, connections
@api_view(['GET','POST'])
def index(request):
    if request.method=='GET':
        request_data=[]

        navercafe=Navercafe.objects.all().reverse()[:10]


        # return Response(data=request_data, status=status.HTTP_200_OK)
        serializer = NavercafeSerializer(navercafe, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        product = request.data.get('product', None)
        tablet = request.data.get('tablet', None)
        navercafe_ipad = request.data.get('navercafe_ipad',None)
        if product:
            for cur_product in product:
                id = cur_product.get("id",None)
                category = cur_product.get("category",None)
                manufacturer = cur_product.get("manufacturer",None)
                model_name = cur_product.get("model_name",None)
                generation = cur_product.get("generation",None)
                display = cur_product.get("display",None)
                release_date = cur_product.get("release_date",None)
                Product(id=id, category=category, manufacturer=manufacturer, model_name=model_name, generation=generation , display=display,release_date=release_date).save()
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
                print(cur_data)
                print("###################")
                id = cur_data.get("id", None)
                category = "태블릿"
                # category = cur_data.get("category",None)
                manufacturer = "애플"
                # manufacturer = cur_data.get("manufacturer",None)
                model_name = cur_data.get("model_name",None)
                generation = cur_data.get("generation",None)
                display = cur_data.get("display",None)
                cellular = cur_data.get("cellular",None)
                storage = cur_data.get("storage",None)
                price = cur_data.get("price",None)
                # region = cur_data.get("region",None)
                date = cur_data.get("date",None)
                date =datetime.datetime.strptime(date,'%Y.%m.%d. %H:%M')
                date= date.date()
                link = cur_data.get("link",None)
                img_src = cur_data.get("img_src",None)
                is_sell = False
                title = cur_data.get("title",None)
                contents = cur_data.get("contents",None)
                # is_sell = cur_data.get("is_sell",None)

                if display is "":
                    display=None
            # print(date.date()))
                # 타이틀, 가격, 내용, 아이디, 날짜, 이미지주소, 링크
                Navercafe(id=id,category=category, manufacturer=manufacturer, model_name=model_name, generation=generation,
                          display=display,cellular=cellular,storage=storage,price=price,date=date,link=link,img_src=img_src,is_sell=is_sell,title=title,contents=contents).save()

            pass
        return Response(status=status.HTTP_200_OK)

def my_sql(key, value):
    cursor = connection.cursor()
    query = 'select * from navercafe limit 10;'
    cursor.execute(str)
    row = dictfetchall(cursor)
    return row
    # if key == 'user':
    #     str = 'SELECT username FROM `auth_user` WHERE id IN (' + value + ')'
    #     cursor.execute(str)
    #     row = dictfetchall(cursor)
    #     return row
    # if key == 'getuserid':
    #     cursor.execute('SELECT userid FROM `api_rating` WHERE id=%s;',[value])
    #     row = cursor.fetchall()
    #     return row


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
