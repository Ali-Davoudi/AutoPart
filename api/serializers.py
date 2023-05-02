from rest_framework import serializers
from auth_module.models import User
from blog_module.models import Blog
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
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class BrandSerializer(serializers.ModelSerializer): # Make nested wirtable for category and brand
#     class Meta:
#         model = ProductBrand
#         fields = ['id', 'title']
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductCategory
#         fields = ['id', 'title']
