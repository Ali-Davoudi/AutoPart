from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from utils.validators import validate_email


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='پست الکترونیکی * ',
        widget=forms.EmailInput(attrs={'placeholder': 'آدرس ایمیل'}),
        error_messages={'required': 'لطفا پست الکترونیکی خود را وارد نمایید.'},
        validators=[validators.MinLengthValidator(10, 'ایمیل وارد شده نباید کمتر از 10 کاراکتر باشد.'),
                    validators.MaxLengthValidator(80, 'ایمیل وارد شده نمی تواند بیشتر از 80 کاراکتر باشد.'),
                    validate_email
                    ]
    )
    password = forms.CharField(
        label='کلمه عبور * ',
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}),
        error_messages={'required': 'لطفا کلمه عبور را وارد نمایید.'},
        validators=[validators.MinLengthValidator(5, 'کلمه عبور باید بیشتر از 5 کاراکتر باشد.')]
    )
    confrim_password = forms.CharField(
        label='تکرار کلمه عبور * ',
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور'}),
        error_messages={'required': 'لطفا کلمه عبور را وارد نمایید.'},
    )

    def clean_confrim_password(self):
        password = self.cleaned_data.get('password')
        confrim_password = self.cleaned_data.get('confrim_password')

        if password == confrim_password:
            return password
        else:
            raise ValidationError('عدم سازگاری بین کلمه عبور با تکرار کلمه عبور وجود دارد.')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='پست الکترونیکی * ',
        widget=forms.EmailInput(attrs={'placeholder': 'آدرس ایمیل'}),
        error_messages={'required': 'لطفا پست الکترونیکی خود را خالی نگذارید.'}
    )
    password = forms.CharField(
        label='کلمه عبور * ',
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}),
        error_messages={'required': 'لطفا کلمه عبور را خالی نگذارید.'}
    )


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        label='پست الکترونیکی',
        widget=forms.EmailInput(attrs={'placeholder': 'آدرس ایمیل'}),
        error_messages={'required': 'لطغا آدرس ایمیل را خالی نگذارید.'}
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}),
        error_messages={'required': 'لطغا کلمه عبور را خالی نگذارید.'}
    )
    confrim_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور'}),
        error_messages={'required': 'لطغا تکرار کلمه عبور را خالی نگذارید.'}
    )

    def clean_confrim_password(self):
        password = self.cleaned_data.get('password')
        confrim_password = self.cleaned_data.get('confrim_password')

        if password == confrim_password:
            return password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مقایرت دارند.')
