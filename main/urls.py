from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login, name="login"),
    path('upload-certificate', views.upload_certificate, name="upload-certificate"),
    path('sign-up', views.sign_up, name="sign-up"),
    path('add-rating', views.add_rating, name="add-rating"),
    path('admin/invite-key-gen', views.invite_key_gen, name="admin/invite-key-gen"),
    path("logout/", LogoutView.as_view(), name="logout"),
]