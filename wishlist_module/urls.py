from django.urls import path
from wishlist_module.views import user_wishlist, AddToWishListView, remove_favourite_product

urlpatterns = [
    path('my-wishlist', user_wishlist, name='user_wishlist'),
    path('my-wishlist/add-to-wishlist', AddToWishListView.as_view(), name='add_to_wishlist'),
    path('my-wishlist/remove-product-from-wishlist', remove_favourite_product, name='remove_favourite_product')
]
