from django.urls import path

from basket_order_module.views import AddProductToOrder, user_basket_order, remove_an_order

urlpatterns = [
    path('my-basket-order/add-to-order', AddProductToOrder.as_view(), name='add_to_order'),
    path('my-basket-order', user_basket_order, name='user_basket_order'),
    path('my-basket-order/remove-order', remove_an_order, name='remove_order'),
]
