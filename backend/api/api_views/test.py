from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TabletSerializer, ProductSerializer
from api.models import Tablet,Product
@api_view(['GET','POST'])
def index(request):
    if request.method=='GET':
        # tablet = Tablet.objects.all()
        # serializer = TabletSerializer(tablet, many=True)
        # return Response(data=serializer.data, status=status.HTTP_200_OK)
        #
        request_data=["get"]
        return Response(data=request_data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        product = request.data.get('product', None)
        tablet = request.data.get('tablet', None)
        if product:
            for cur_product in product:
                id = cur_product.get("id",None)
                category = cur_product.get("category",None)
                manufacturer = cur_product.get("manufacturer",None)
                model_name = cur_product.get("model_name",None)
                generation = cur_product.get("generation",None)
                display = cur_product.get("display",None)
                release_date = cur_product.get("release_date",None)
                print(cur_product)
                Product(id=id, category=category, manufacturer=manufacturer, model_name=model_name, generation=generation , display=display,release_date=release_date).save()
        if tablet:
            for cur_tablet in tablet:
                product_id = cur_tablet.get("product_id", None)
                key_name = cur_tablet.get("key_name",None)
                cellular = cur_tablet.get("cellular",None)
                storage = cur_tablet.get("storage",None)
                price = cur_tablet.get("price",None)
                query = cur_tablet.get("query",None)
                print(key_name)
                Tablet(product_id=product_id,key_name=key_name, cellular=cellular, storage=storage, price=price,query=query).save()

        return Response(status=status.HTTP_200_OK)