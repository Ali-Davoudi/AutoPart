from django.urls import path

from contact_module.views import ContactView

urlpatterns = [
    path('contact-us', ContactView.as_view(), name='contact_page'),
]
