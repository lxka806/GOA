from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def all_users(req):
    return render(req, "all_users.html", {
        "all_users": User.objects.all()
    })


def register_user(req):
    if req.method == 'POST':

        name = req.POST.get('user_name')
        email = req.POST.get('user_email')
        password = req.POST.get('user_password')
        age = req.POST.get('user_age')

        new_user = User( 
            name=name, 
            email=email, 
            password=password, 
            age=age
            )
        new_user.save()  

        return redirect('main_user')

    return render(req, 'user_registation.html')



def login_user(req):
    context = {
        "errors": []
    }

    if req.method == "POST":
        email = req.POST.get("email")
        password = req.POST.get("password")

        try:
            user = User.objects.get(email=email)

            if user.password == password:
                req.session["user_id"] = user.id
                req.session["user_name"] = user.name

                return redirect("main_user")

            else:
                context["errors"].append("Wrong password")

        except:
            context["errors"].append("User does not exist")

    return render(req, "login.html", context)