from django.urls import path, include

from api.views import ArticleList, ArticleDetail, UserList, UserDetail, ProductList, ProductDetail

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('blog/', ArticleList.as_view(), name='blog'),
    path('blog/<int:pk>', ArticleDetail.as_view(), name='blog_detail'),
    path('users/', UserList.as_view(), name='users'),
    path('users/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]
