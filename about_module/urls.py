from django.urls import path
from about_module.views import AboutUsTemplateView

urlpatterns = [
    path('about-us', AboutUsTemplateView.as_view(), name='about_page')
]
