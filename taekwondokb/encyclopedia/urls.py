from django.urls import path
from . import views


app_name = 'encyclopedia'
urlpatterns = [
    path('', views.toms, name='volumes-list'),
    path('<slug:volume>/', views.volume, name='volume'),
    path('<slug:volume>/<int:page>/', views.page, name='page'),
]