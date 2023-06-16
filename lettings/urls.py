from django.urls import path

from lettings.views import letting, index


BASE_URL = "lettings"

urlpatterns = [
    path(f"{BASE_URL}/", index, name="lettings_index"),
    path(f"{BASE_URL}/<int:letting_id>/", letting, name="letting"),
]
