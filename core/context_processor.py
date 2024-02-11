from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReveiw, WishList_model,  Address
from django.db.models import Min, Max
from django.contrib import messages


def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()

    min_max_price = Product.objects.aggregate(Min("price"), Max("price"))

    try:
        wishlist = WishList_model.objects.filter(user=request.user)
    except:
        messages.warning(request, "You need to login before access to wishlist")
        wishlist = 0


    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None

    return {
        'categories': categories,
        'wishlist': wishlist,
        'vendors': vendors,
        'address': address,
        'min_max_price': min_max_price
    }