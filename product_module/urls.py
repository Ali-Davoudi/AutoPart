from django.urls import path
from product_module.views import ProductListView, ProductDetailView, AddProductComment, SearchProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/category/<cat>', ProductListView.as_view(), name='product_categories'),
    path('products/brand/<brand>', ProductListView.as_view(), name='product_brands'),
    path('products/<pk>/<name>', ProductDetailView.as_view(), name='product_detail'),
    path('products/add-product-comment', AddProductComment.as_view(), name='add_product_comment'),
    path('products/all', SearchProductListView.as_view(), name='search_products')
]
