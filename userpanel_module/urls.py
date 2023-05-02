from django.urls import path
from userpanel_module.views import UserPanelDashboardView, order_factor_pdf

urlpatterns = [
    path('dashboard', UserPanelDashboardView.as_view(), name='dashboard'),
    path('dashboard/order-factor/', order_factor_pdf, name='order_factor_pdf')
]
