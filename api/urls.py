from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from api.views import UserList, UserDetail, ProductList, ProductDetail, RevokeToken

urlpatterns = [
    # path('api-auth', include('rest_framework.urls')),
    path('auth-token/', obtain_auth_token),
    path('revoke-token/', RevokeToken.as_view()),
    path('users/', UserList.as_view(), name='users'),
    path('users/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]
