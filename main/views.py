from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import django.contrib.auth as da
import main.models as model

def index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    context = {'username': username}
    return render(request, 'main/index.html', context)

def login(request):
    context = { 'error': ''}
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['password']
        user = da.authenticate(request, username=username, password=password)
        if user is not None:
            da.login(request, user)
            return redirect('/')
        else:
            context= {'error': 'invalid login'}
    return render(request, 'main/sign_in.html', context)
         
def sign_up(request):
    da.logout(request)
    invite_key_status = ""
    error = ""
    if request.method == 'POST':
        if request.POST['invite_key_status'] != 'OK':
            invite_key = request.POST['invite_key']
            if model.InviteKey.objects.filter(invite_key__exact=invite_key).count():
                    invite_key_status = "OK"
            else:
                error = 'invalid key'
        else:
            full_name = request.POST['full_name'].split(' ')
            first_name = ''
            last_name = ''
            first_name = full_name[0]
            if len(full_name) > 1:
                last_name = full_name[1]
            if len(first_name) == 0 or len(last_name) == 0:
                error = 'enter your full name'
                context = {"invite_key" : "OK", "error": error}
                return render(request, 'main/sign_up.html', context)

            faculty = request.POST.get('faculty')
            if faculty == None:
                error = 'enter your faculty'
                context = {"invite_key" : "OK", "error": error}
                return render(request, 'main/sign_up.html', context)
                
            email = request.POST['email']
            login = request.POST['login']
            password = request.POST['password']

            user = User.objects.create_user(login, email, password, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('/')
    context = {"invite_key" : invite_key_status, "error": error}
    return render(request, 'main/sign_up.html', context)
