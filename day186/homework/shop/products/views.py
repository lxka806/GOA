from django.shortcuts import render
from .models import Product

# Create your views here.
def home(req):
    return render(req, 'home.html', {
        'all_products': Product.objects.all()
    })
