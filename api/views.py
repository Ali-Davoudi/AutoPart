from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from api.permissions import IsStaffOrReadOnly
from api.serializers import ArticleSerializer, UserSerializer, ProductSerializer
from auth_module.models import User
from blog_module.models import Blog
from product_module.models import Product


class ProductList(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsStaffOrReadOnly]


class ProductDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]


class ArticleList(ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Blog.objects.all()


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Blog.objects.all()


class UserList(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
