from django import views
from django.urls import path
from core.views import index, product_list_view, category_list_view, category_product_list_view, vendor_list_view, vendor_detail_view, product_detail_view, tag_list, ajax_add_review, search_view

app_name = "core"

urlpatterns = [
    path('', index, name="index"),
    path('products/', product_list_view, name="product-list"),
    path('product/<pid>/', product_detail_view, name="product-detail"),

    path('category/', category_list_view, name="category-list"),
    path('category/<cid>/', category_product_list_view, name="category-product-list"),

    path('vendors/', vendor_list_view, name="vendor-list"),
    path('vendor/<vid>/', vendor_detail_view, name="vendor-detail"),

    path('products/tag/<slug:tag_slug>/', tag_list, name="tags"),

    path('ajax-add-review/<int:pid>/', ajax_add_review, name='ajax-add-review'),
    path('search', search_view, name="search")
]
