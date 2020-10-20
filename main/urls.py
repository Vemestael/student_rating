from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('sign-up', views.sign_up),
    path('add-rating', views.add_rating),
    path('admin/invite-key-gen', views.invite_key_gen),
    path("logout/", LogoutView.as_view(), name="logout"),
]