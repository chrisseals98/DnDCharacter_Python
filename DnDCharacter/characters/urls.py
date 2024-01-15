from django.urls import path
from . import views

app_name = "characters"
urlpatterns = [
    path("", views.ListView.as_view(), name="list"),
    path("<int:pk>", views.DetailedView.as_view(), name="detail")
]