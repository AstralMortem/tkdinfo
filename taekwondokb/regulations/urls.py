from django.urls import path
from . import views


app_name = 'regulations'
urlpatterns = [
    path('', views.belts, name='belts-list'),
    path('<slug:belt_kup>/', views.regulation, name='regulation'),
]