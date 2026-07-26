from django.shortcuts import render
from .models import Product

def products(request):
    products = Product.objects.all()
    return render(request, "home.html", {
        "products": products
    })