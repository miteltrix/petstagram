from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('original', views.landing_page, name='landing')
]