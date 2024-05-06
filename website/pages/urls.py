from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path ('dataset/', views.dataset, name='dataset'),
]