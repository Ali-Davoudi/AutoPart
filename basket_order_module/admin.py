from django.contrib import admin
from basket_order_module.models import UserBasketOrder, UserBasketOrderDetail


class UserBasketOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'payment_date', 'is_paid']
    search_fields = ['user__first_name', 'user__last_name', 'user__username', 'user__email']


class UserBasketOrderDetailAdmin(admin.ModelAdmin):
    list_display = ['user_basket_order', 'product', 'product_count', 'final_price']


admin.site.register(UserBasketOrder, UserBasketOrderAdmin)
admin.site.register(UserBasketOrderDetail, UserBasketOrderDetailAdmin)
