from rest_framework import serializers
from api.models import Tablet
class TabletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablet
        fields = '__all__'
        # fields = ('id', 'model_name', 'memory_gb','release_year','price','cellular')