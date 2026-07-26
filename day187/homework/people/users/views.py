from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def all_user(req):
    context = {
        'all_users': User.objects.all()
    }
    return render(req, "users_index.html", context)

def register_user(req):
    if req.method == 'POST':

        email = req.POST.get('user_email')
        username = req.POST.get('user_name')
        age = req.POST.get('user_age')
        password = req.POST.get('user_password')

        new_user = User(username=username, age=age, email=email, password=password)
        new_user.save()

        return redirect('main_users')
    return render(req, 'user_registration.html',)

def login_user(req):
    context = {
        'errors': []
    }

    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')

        try:
            found_user = User.objects.get(email=email, password=password)
            context['errors'] = []

            User.objects.update(is_curent_user=False)
            found_user.is_curent_user = True
            found_user.save()

            return redirect('main_users')
        except:
            context['errors'] = ['invalid email or password']

    return render(req, 'user_login.html', context)

def user_profile(req):
    try:
        context = {
            'curent_user': User.objects.get(is_curent_user=True)
        }
    except:
        context = {
            'curent_user': None
        }
    return render(req, 'user_profile.html', context)

def logout_user(req):
    User.objects.update(is_curent_user=False)
    return redirect('main_users')

def edit_user(req):
    try:
        context = {
            'current_user': User.objects.get(is_curent_user = True)
        }
    except:
        context = {
            'current_user': None
        }

    if req.method == "POST":
        
        email = req.POST.get('user_email')
        username = req.POST.get('user_name')
        age = req.POST.get('user_age')
        password = req.POST.get('user_password')

        current_user = User.objects.get(is_curent_user = True)

        if email != '':
            current_user.email = email
            current_user.save()

        if username != '':
            current_user.username = username
            current_user.save()

        if age != '':
            current_user.age = age
            current_user.save()
        
        if password != '':
            current_user.password = password
            current_user.save()

        return redirect('user_profile')

    return render(req, 'user_edit.html', context)