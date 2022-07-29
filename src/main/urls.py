from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework import routers

from main import drf_views
from main import views

# Django REST routes
router = routers.DefaultRouter()
router.register(r'faculty', drf_views.FacultyAPI)
router.register(r'rating', drf_views.RatingAPI)
router.register(r'extra-point', drf_views.ExtraPointAPI)
router.register(r'invite-key', drf_views.InviteKeyAPI)
router.register(r'excel-file', drf_views.ExcelFileAPI)
router.register(r'certificate', drf_views.CertificateAPI)

urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('login', views.Login.as_view(), name="login"),
    path('get-details', views.GetDetails.as_view(), name="get-details"),
    path('upload-certificate', views.UploadCertificate.as_view(), name="upload-certificate"),
    path('sign-up', views.SignUp.as_view(), name="sign-up"),
    path('add-rating', views.AddRating.as_view(), name="add-rating"),
    path('admin/invite-key-gen', views.InviteKeyGen.as_view(), name="admin/invite-key-gen"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('check-certificate', views.CheckCertificate.as_view(), name="check-certificate"),
    path('change-rating', views.ChangeRating.as_view(), name="change-rating"),
    path('change-from-file', views.ChangeFromFile.as_view(), name="change-from-file"),
    path('profile', views.Profile.as_view(), name="profile"),
    # Django REST routes
    path('api/', include(router.urls))
]
