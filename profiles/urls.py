from django.urls import path

from profiles import views

app_name = "profiles"

urlpatterns = [
    path("", views.list, name="list"),
    path("<str:username>/", views.detail, name="detail"),
]
