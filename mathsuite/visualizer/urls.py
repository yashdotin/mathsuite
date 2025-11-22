from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='visualizer_index'),
    path('plot/', views.plot_function, name='visualizer_plot'),
]
