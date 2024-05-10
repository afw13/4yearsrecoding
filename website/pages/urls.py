from django.urls import path
from . import views
from pages.views import dataset_view

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('dataset/', dataset_view, name='dataset'),
]