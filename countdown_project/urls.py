from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("countdown.urls")),  # Include all countdown URLs at root
]
