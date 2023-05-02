from django.db import models
from utils.validators import validate_email


class Contact(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='نام کاربر')
    email = models.EmailField(validators=[validate_email], verbose_name='ایمیل کاربر')
    subject = models.CharField(max_length=350, null=True, blank=True, verbose_name='موضوع پیام')
    message = models.TextField(verbose_name='متن پیام')
    response = models.TextField(null=True, blank=True, verbose_name='متن پاسخ پیام توسط ادمین')
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده / نشده')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس های کاربران'

    def __str__(self):
        return self.fullname
