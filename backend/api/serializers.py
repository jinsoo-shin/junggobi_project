from rest_framework import serializers
from api.models import Tablet, Product,Navercafe
class TabletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablet
        fields = '__all__'
        # fields = ('id', 'model_name', 'memory_gb','release_year','price','cellular')
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class NavercafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navercafe
        fields = '__all__'
