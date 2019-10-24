from rest_framework import serializers
from api.models import Tablet, Product, ProductInfo
class TabletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablet
        fields = '__all__'
        # fields = ('id', 'model_name', 'memory_gb','release_year','price','cellular')
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Product_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = '__all__'