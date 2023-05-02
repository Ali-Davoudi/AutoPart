from django.urls import path
from service_module.views import ServiceTemplateView

urlpatterns = [
    path('services', ServiceTemplateView.as_view(), name='service_page')
]
