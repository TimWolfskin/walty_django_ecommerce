# from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from taggit.models import Tag
from django.db.models import Avg #Count
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReveiw, WishList, Address
from core.forms import ProductReviewForm


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



def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        "category": category,
        "products": products
    }
    return render(request, "core/category-product-list.html", context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()

    context = {
        "vendors": vendors
    }
    return render(request, "core/vendor-list.html", context)



def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published")

    context = {
        "vendor": vendor,
        "products": products
    }
    return render(request, "core/vendor-detail.html", context)



def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    # product = get_object_or_404(Product, pid=pid)
    products = Product.objects.filter(category=product.category).exclude(pid=pid)

    #getting all reviews related to a product
    reviews = ProductReveiw.objects.filter(product=product).order_by("-date")

    #getting average review
    average_rating = ProductReveiw.objects.filter(product=product).aggregate(rating=Avg('rating'))

    #review form
    review_form = ProductReviewForm()

    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReveiw.objects.filter(user=request.user, product=product).count()

        if user_review_count > 0:
            make_review = False

    product_image = product.product_images.all()

    context = {
        "product": product,
        "review_form": review_form,
        "make_review": make_review,
        "reviews": reviews,
        "average_rating": average_rating,
        "product_image": product_image,
        "produts": products
    }
    return render(request, 'core/product-detail.html', context)



def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-id")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        "products": products,
        "tag": tag
    }
    return render(request, "core/tag.html", context)


def ajax_add_review(request, pid):
    product = Product.objects.get(pk=pid)
    user = request.user

    review = ProductReveiw.objects.create(
        user=user,
        product=product,
        review = request.POST['review'],
        rating = request.POST['rating'],
    )
    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }
    average_reviews = ProductReveiw.objects.filter(product=product).aggregate(rating=Avg("rating"))

    return JsonResponse (
        {
            'bool': True,
            'context': context,
            'average_reviews': average_reviews
        }
    )


def search_view(request):
    query = request.GET.get("q")

    products = Product.objects.filter(title__icontains=query).order_by("-date")

    context = {
        "products": products,
        "query": query
    }
    return render(request, "core/search.html", context)
