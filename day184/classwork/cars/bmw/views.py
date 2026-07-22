from django.shortcuts import render, redirect, get_object_or_404
from .models import BMW


def cars_list(request):
    context = {
        "all_cars": BMW.objects.all()
    }

    return render(request, "bmw_index.html", context)


def car_details(request, id):
    context = {
        "car": get_object_or_404(BMW, id=id)
    }

    return render(request, "car_details.html", context)


def delete_car(request, id):
    car = get_object_or_404(BMW, id=id)
    car.delete()

    return redirect("/bmw/")