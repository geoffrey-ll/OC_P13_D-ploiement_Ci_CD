from django.urls import path

from profiles.views import profile, index


BASE_URL = "profiles"

urlpatterns = [
    path(f"{BASE_URL}/", index, name="profiles_index"),
    path(f"{BASE_URL}//<str:username>/", profile, name="profile"),
]
