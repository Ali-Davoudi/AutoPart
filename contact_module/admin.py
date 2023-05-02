from django.contrib import admin

from contact_module.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'create_date', 'is_read_by_admin']


admin.site.register(Contact, ContactAdmin)
