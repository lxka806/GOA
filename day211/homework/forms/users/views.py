from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'user_register.html', {
                'register_form': form
            }) 
    return render(request, 'user_register.html', {
        'register_form': UserCreationForm()
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
        else:
            return render(request, 'user_login.html', {
                'login_form': form
            })
    return render(request, 'user_login.html', {
        'login_form': AuthenticationForm()
    })