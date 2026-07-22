from django.shortcuts import render, redirect
from .models import Phone


def all_phones(req):
    context = {
        "all_phones": Phone.objects.all()
    }

    return render(req, "index.html", context)


def phone_details(req, id):
    phone_detail = Phone.objects.get(id=id)

    return render(req, "phone_details.html", {
        "phone": phone_detail
    })


def delete_phone(req, id):
    phone = Phone.objects.get(id=id)
    phone.delete()

    return redirect("/phone/")