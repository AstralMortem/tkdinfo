from django.urls import path, include
from . import views


app_name = 'restapi'

urlpatterns = [
    path('',views.index, name='index'),
    path('docs/', views.docs, name='docs'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('token/', views.obtain_token, name='token'),


    path('api/v1/<uuid:token>/encyclopedia/', views.VolumesList.as_view(), name='api-volume-list'),
    path('api/v1/<uuid:token>/encyclopedia/<int:tom>/', views.VolumeDetail.as_view(), name='api-volume-detail'),
    path('api/v1/<uuid:token>/encyclopedia/<int:tom>/<int:page>', views.PageDetail.as_view(), name='api-page-detail'),

    path('api/v1/<uuid:token>/belts/', views.BeltList.as_view(), name='api-belt-list'),
    path('api/v1/<uuid:token>/belts/<slug:kupslug>', views.RegulationView.as_view(), name='api-regulation-view'),
]