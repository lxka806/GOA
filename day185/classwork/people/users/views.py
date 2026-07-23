from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def register(req):
    if req.method == "POST":
        User.objects.create(
            fullname=req.POST.get("fullname"),
            email=req.POST.get("email"),
            age=req.POST.get("age")
        )
        return redirect("/register/")

    return render(req, "register.html")