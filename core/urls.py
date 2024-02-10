from django import views
from django.urls import path, include
from core.views import index, product_list_view, category_list_view, category_product_list_view, vendor_list_view, vendor_detail_view, product_detail_view, tag_list, ajax_add_review, search_view, filter_product, add_to_cart, cart_view, delete_item_from_cart, update_cart, checkout_view, payment_completed_view, payment_failed_view, customer_dashboard, order_detail, make_address_default

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
    path('search', search_view, name="search"),
    path('filter-products/', filter_product, name="filter-product"),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('cart/', cart_view, name="cart"),
    path('delete-from-cart/', delete_item_from_cart, name="delete-from-cart"),
    path('update-cart/', update_cart, name="update-cart"),
    path('checkout/', checkout_view, name="checkout"),
    path('paypal/', include("paypal.standard.ipn.urls")),

    path('payment-completed/', payment_completed_view, name="payment-completed" ),
    path('payment-failed/', payment_failed_view, name="payment-failed"),
    path('dashboard/', customer_dashboard, name="dashboard"),
    path('dashboard/order/<int:id>', order_detail, name="order-detail"),
    path('make-default-address/', make_address_default, name="make-default-address")
]
