from django.urls import path
from crm_administration import views


app_name = 'crm_administration'

urlpatterns = [
    path('', views.loading_page, name='loading_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_factory/', views.add_factory, name='add_factory'),
    path('update_factory/<int:pk>/', views.update_factory, name='update_factory'),
    path('delete_factory/<int:pk>/', views.delete_factory, name='delete_factory'),

    path('add_deposit/', views.add_deposit, name='add_deposit'),
]
