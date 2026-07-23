from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def add_product(req):
    if req.method == "POST":
        name = req.POST.get("name")
        price = req.POST.get("price")


        Product.objects.create(
            name=name,
            price=price
        )

        return redirect("/products/add/")

    return render(req, "products.html")