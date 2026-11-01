from django.urls import path

from . import views

app_name = "paints"

urlpatterns = [
    path("", views.paints_list, name="list"),
    path("<int:paint_id>/", views.paint_detail, name="detail"),
]
