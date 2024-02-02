from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Count
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReveiw, WishList, Address


def index(request):
    # products = Product.objects.all()
    products = Product.objects.filter(product_status="published", featured=True)

    context = {
        "products": products
    }
    return render(request, 'core/index.html', context)



def product_list_view(request):
    products = Product.objects.filter(product_status="published", featured=True)

    context = {
        "products": products
    }
    return render(request, 'core/product-list.html', context)



def category_list_view(request):
    categories = Category.objects.all() #.annotate(product_count=Count("product"))

    context = {
        "categories": categories
    }
    return render(request, 'core/category-list.html', context)
