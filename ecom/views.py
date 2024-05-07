from django.shortcuts import render

def home(request):
    latest_product_list = Product.objects.order_by("-upload_date")[:5]
    context = { "title": "Home", "latest_product_list": latest_product_list }
    return render(request, "ecom/home.html", context=context)

def cart(request):
    context = { "title": "Your Cart" }
    return render(request, "ecom/cart.html", context=context)

def detail(request, product_id):
    context = { "title": product_id, "product_id": product_id }
    return render(request, "ecom/detail.html", context=context)
