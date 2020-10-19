from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('sign-up', views.sign_up),
    path("logout/", LogoutView.as_view(), name="logout"),
]