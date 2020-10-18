from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, 'main/sign_in.html')
    
def sign_up(request):
    return render(request, 'main/sign_up.html')