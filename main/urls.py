from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login, name="login"),
    path('get-details', views.get_details, name="add-rating"),
    path('upload-certificate', views.upload_certificate, name="upload-certificate"),
    path('sign-up', views.sign_up, name="sign-up"),
    path('add-rating', views.add_rating, name="add-rating"),
    path('admin/invite-key-gen', views.invite_key_gen, name="admin/invite-key-gen"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('check-certificate', views.check_certificate, name="check-certificate"),
    path('change-rating', views.change_rating, name="change-rating"),
    path('change-from-file', views.change_from_file, name="change-from-file"),
    path('profile', views.profile, name="profile"),
]
