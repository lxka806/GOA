from django.shortcuts import render

# Create your views here.
admins_database = [
    {'id': 0, 'admin_name': 'aleksandre', 'role': 'main_staff'},
    {'id': 1, 'admin_name': 'giorgi', 'role': 'moderator'},
    {'id': 2, 'admin_name': 'nika', 'role': 'support'},
    {'id': 3, 'admin_name': 'luka', 'role': 'developer'},
    {'id': 4, 'admin_name': 'saba', 'role': 'moderator'},
    {'id': 5, 'admin_name': 'dato', 'role': 'support'},
    {'id': 6, 'admin_name': 'levani', 'role': 'developer'},
    {'id': 7, 'admin_name': 'irakli', 'role': 'moderator'},
    {'id': 8, 'admin_name': 'gio', 'role': 'support'},
    {'id': 9, 'admin_name': 'tornike', 'role': 'developer'},
    {'id': 10, 'admin_name': 'vano', 'role': 'moderator'},
    {'id': 11, 'admin_name': 'zura', 'role': 'support'},
    {'id': 12, 'admin_name': 'bacho', 'role': 'developer'},
    {'id': 13, 'admin_name': 'otari', 'role': 'moderator'},
    {'id': 14, 'admin_name': 'temuri', 'role': 'support'},
    {'id': 15, 'admin_name': 'andria', 'role': 'developer'},
    {'id': 16, 'admin_name': 'gabrieli', 'role': 'moderator'},
    {'id': 17, 'admin_name': 'lasha', 'role': 'support'},
    {'id': 18, 'admin_name': 'mate', 'role': 'developer'},
    {'id': 19, 'admin_name': 'sandri', 'role': 'moderator'},
]

def All_Admin(req):
    return render(req, 'index.html', {'admins_database': admins_database})

def Admin(req, id):
    one_Admin = admins_database[id]
    return render(req, 'admin.html', one_Admin)