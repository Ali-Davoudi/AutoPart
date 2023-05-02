from django.urls import path
from home_module.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home_page')
]
