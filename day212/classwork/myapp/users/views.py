from django.shortcuts import render, redirect
from .forms import RegisterForm

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = RegisterForm()

    return render(request, "register_user.html", {"form": form})