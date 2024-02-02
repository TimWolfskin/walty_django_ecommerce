from django.urls import path
from core.views import index, product_list_view

app_name = "core"

urlpatterns = [
    path('', index, name="index"),
    path('products/', product_list_view, name="product-list")
]
