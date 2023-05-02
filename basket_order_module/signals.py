from django.db.models.signals import post_save
from django.dispatch import receiver
from threading import Timer
from basket_order_module.models import UserBasketOrder, UserBasketOrderDetail
from product_module.models import Product


@receiver(post_save, sender=UserBasketOrder)
def delete_outdate_basket_details(sender, instance, **kwargs):
    def update_field():
        # Checking unpaid basket
        if instance.is_paid is False:
            # Getting user basket details
            user_basket_details = UserBasketOrderDetail.objects.filter(user_basket_order_id=instance.id)
            # Each user basket details for correct calculate products In Stock count
            for detail in user_basket_details:
                product_id = detail.product_id
                product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
                if detail.user_basket_order.is_paid is False:
                    instance.userbasketorderdetail_set.filter(user_basket_order__is_paid=False).delete()
                    product.in_stock += detail.product_count
                    product.save()

    t = Timer(30, update_field)  # 86400 seconds = 1440 minutes = 24 hours | Test: 30 seconds pass to Timer
    t.start()


@receiver(post_save, sender=UserBasketOrderDetail)
def delete_outdate_basket(sender, instance, **kwargs):
    def update_field():
        if instance.user_basket_order.is_paid is False:
            instance.user_basket_order.delete()

    t = Timer(30, update_field)  # 86400 seconds = 1440 minutes = 24 hours
    t.start()

# @receiver(post_save, sender=UserBasketOrder)
# def delete_old_basket_orders(sender, instance, **kwargs):
#     if instance.is_paid is False and instance.created_at < timezone.now() - timezone.timedelta(minutes=30):
#         instance.userbasketorderdetail_set.all().delete()
#         instance.delete()
#
#
# # Get all orders with is_paid as False and older than 30 minutes
# old_orders = UserBasketOrder.objects.filter(is_paid=False,
#                                             created_at__lte=timezone.now() - timezone.timedelta(
#                                                 minutes=3))
# # Loop through each old order and delete its order details
# for old_order in old_orders:
#     old_order.userbasketorderdetail_set.all().delete()
#
# # Delete the old orders
# old_orders.delete()