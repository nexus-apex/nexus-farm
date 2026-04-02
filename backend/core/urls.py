from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('crops/', views.crop_list, name='crop_list'),
    path('crops/create/', views.crop_create, name='crop_create'),
    path('crops/<int:pk>/edit/', views.crop_edit, name='crop_edit'),
    path('crops/<int:pk>/delete/', views.crop_delete, name='crop_delete'),
    path('farmfields/', views.farmfield_list, name='farmfield_list'),
    path('farmfields/create/', views.farmfield_create, name='farmfield_create'),
    path('farmfields/<int:pk>/edit/', views.farmfield_edit, name='farmfield_edit'),
    path('farmfields/<int:pk>/delete/', views.farmfield_delete, name='farmfield_delete'),
    path('harvests/', views.harvest_list, name='harvest_list'),
    path('harvests/create/', views.harvest_create, name='harvest_create'),
    path('harvests/<int:pk>/edit/', views.harvest_edit, name='harvest_edit'),
    path('harvests/<int:pk>/delete/', views.harvest_delete, name='harvest_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
