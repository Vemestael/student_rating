from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import Index, UploadCertificate, GetDetails, Login, SignUp, InviteKeyGen, AddRating, CheckCertificate, \
    ChangeRating, ChangeFromFile, Profile

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('login', Login.as_view(), name="login"),
    path('get-details', GetDetails.as_view(), name="add-rating"),
    path('upload-certificate', UploadCertificate.as_view(), name="upload-certificate"),
    path('sign-up', SignUp.as_view(), name="sign-up"),
    path('add-rating', AddRating.as_view(), name="add-rating"),
    path('admin/invite-key-gen', InviteKeyGen.as_view(), name="admin/invite-key-gen"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('check-certificate', CheckCertificate.as_view(), name="check-certificate"),
    path('change-rating', ChangeRating.as_view(), name="change-rating"),
    path('change-from-file', ChangeFromFile.as_view(), name="change-from-file"),
    path('profile', Profile.as_view(), name="profile"),
]
