from django.contrib import admin
from django.urls import path, include
from .views import dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("converter/", include("converter.urls")),
    path("calculator/", include("calculator.urls")),
    path("geometry/", include("geometry.urls")),
    path("visualizer/", include("visualizer.urls")),
    path("admin/", admin.site.urls),
]
