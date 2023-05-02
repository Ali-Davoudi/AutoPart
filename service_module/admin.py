from django.contrib import admin
from service_module.models import Service, ServiceDetail


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_active']


class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceDetail, ServiceDetailAdmin)
