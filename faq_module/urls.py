from django.urls import path
from faq_module.views import FaqTemplateView

urlpatterns = [
    path('faq', FaqTemplateView.as_view(), name='faq_page')
]
