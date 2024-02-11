from company import views
from django.urls import path

app_name = 'company'

urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('ajax-contact-form/', views.ajax_contact_form, name="ajax-contact-form")
]
