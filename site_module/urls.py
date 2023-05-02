from django.urls import path
from site_module.views import PrivacyPolicyTemplateView

urlpatterns = [
    path('privacy-policy', PrivacyPolicyTemplateView.as_view(), name='privacy_policy_page')
]
