from django.urls import path

from lettings import views

app_name = "lettings"

urlpatterns = [
    path("", views.list, name="list"),
    path("<int:letting_id>/", views.detail, name="detail"),
]
