from rest_framework import serializers


from app1.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'