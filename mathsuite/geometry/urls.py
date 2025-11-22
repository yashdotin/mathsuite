from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='geometry_index'),
    path('draw/', views.draw_shape, name='geometry_draw'),
]
