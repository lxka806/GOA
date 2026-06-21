from django.shortcuts import render

# Create your views here.
products_database = [
    {'id': 0, 'title': 'ზანგის ღიმილი', 'price': 5.99},
    {'id': 1, 'title': 'Python წიგნი', 'price': 19.99},
    {'id': 2, 'title': 'Gaming Mouse', 'price': 49.99},
    {'id': 3, 'title': 'Mechanical Keyboard', 'price': 89.99},
    {'id': 4, 'title': 'Monitor', 'price': 199.99},
]

def all_products(req):
    context = {
        'products': products_database
    }

    return render(req, 'all_products.html', context)

def product_detail(req, product_id):
    product = products_database[product_id]

    context = {
        'product': product
    }

    return render(req, 'products_detaill.html', context)