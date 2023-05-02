from django.contrib import admin
from faq_module.models import Faq


class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'is_active']
    list_editable = ['is_active']


admin.site.register(Faq, FaqAdmin)
