from django.urls import path
from .views import countdown_view, home_view

app_name = "countdown"  # Namespace para evitar conflitos

urlpatterns = [
    path("", home_view, name="home"),
    path("countdown/", countdown_view, name="countdown"),
]
