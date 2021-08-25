from django.urls import path
from crm_administration import views


app_name = 'crm_administration'

urlpatterns = [
    path('', views.loading_page, name='loading_page'),
    path('dashboard/', views.dashboard, name='dashboard')
]