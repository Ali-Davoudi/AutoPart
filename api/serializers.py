from rest_framework import serializers
from auth_module.models import User
from product_module.models import Product


class ProductSerializer(serializers.ModelSerializer):

    # Show category titles instead of ID
    def get_category(self, obj: Product):
        return list(obj.category.values_list('title', flat=True))

    category = serializers.SerializerMethodField('get_category')

    # Show brand title instead of ID
    def get_brand(self, obj: Product):
        return obj.brand.title

    brand = serializers.SerializerMethodField('get_brand')

    class Meta:
        model = Product
        exclude = ['image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
