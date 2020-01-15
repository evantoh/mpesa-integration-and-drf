from rest_framework import serializers
from .models import MwendaShop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = MwendaShop
        fields = ('id', 'name', 'description', 'price')
