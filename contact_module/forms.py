from django import forms
from django.core import validators
from utils.validators import validate_email


class ContactForm(forms.Form):
    fullname = forms.CharField(
        label='نام و نام خانوادگی * ',
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی', 'name': 'name'}),
        error_messages={'required': 'لطفا قسمت نام و نام خانوادگی را خالی نگذارید!'},
        validators=[
            validators.MaxLengthValidator(40, 'نام و نام خانوادگی نمی تواند بیشتر از 40 کاراکتر باشد.')
        ]
    )
    email = forms.EmailField(
        label='آدرس ایمیل * ',
        widget=forms.EmailInput(attrs={'placeholder': 'پست الکترونیکی', 'name': 'email'}),
        error_messages={'required': 'لطفا قسمت ایمیل را خالی نگذارید!'},
        validators=[validate_email]
    )
    subject = forms.CharField(
        label='موضوع پیام (اختیاری) ',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'موضوع پیام', 'name': 'subject'}),
    )
    message = forms.CharField(
        label='متن پیام * ',
        widget=forms.Textarea(attrs={'placeholder': 'پیام', 'name': 'message', 'class': 'form-control2'}),
        error_messages={'requierd': 'لطفا قسمت متن پیام را خالی نگذارید!'}
    )
