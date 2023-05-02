from django.db import models
from django.utils import timezone
from auth_module.models import User
from product_module.models import Product
from jalali_date import date2jalali


class UserBasketOrder(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='پرداخت شده / پرداخت نشده')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ و زمان ایجاد')
    payment_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ و زمان پرداخت')

    class Meta:
        verbose_name = 'سبد خرید کاربر'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        return str(self.user)

    def calculate_total_amount(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.userbasketorderdetail_set.all():
                total_amount += order_detail.product_count * order_detail.final_price
        else:
            for order_detail in self.userbasketorderdetail_set.all():
                total_amount += order_detail.product_count * order_detail.single_price

        return total_amount

    def get_jalali_date(self):
        return date2jalali(self.payment_date).strftime('%d %B %Y')


class UserBasketOrderDetail(models.Model):
    user_basket_order = models.ForeignKey(to=UserBasketOrder, on_delete=models.PROTECT, verbose_name='سبد خرید کاربر')
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT, verbose_name='محصول')
    product_count = models.PositiveIntegerField(verbose_name='تعداد محصول')
    final_price = models.PositiveBigIntegerField(verbose_name='قیمت نهایی تکی محصول', null=True, blank=True)
    single_price = models.PositiveIntegerField(null=True)

    def save(self, *args, **kwargs):
        # If admin change the product price, This will not affect to the current user basket order detail
        if not self.single_price:
            self.single_price = self.product.sell_price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'جزییات سبد خرید کاربر'
        verbose_name_plural = 'جزییات سبدهای خرید کاربران'

    def __str__(self):
        return str(self.user_basket_order)

    def get_eatch_total_amount(self):
        return self.single_price * self.product_count
