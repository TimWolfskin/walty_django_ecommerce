from django.contrib import admin
from company.models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject']


admin.site.register(ContactUs, ContactUsAdmin)
