from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReveiw, WishList,  Address




def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None

    return {
        'categories': categories,
        'vendors': vendors,
        'address': address
    }