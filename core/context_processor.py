from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReveiw, WishList, Address

def default(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }