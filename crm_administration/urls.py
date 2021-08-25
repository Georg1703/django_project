from django.urls import path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('', views.loading_page, name='loading_page'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
]