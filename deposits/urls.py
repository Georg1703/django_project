from django.urls import path
from deposits import views


app_name = 'deposits'


urlpatterns = [
    path('add/', views.add_deposit, name='add_deposit'),
    path('update/<int:pk>/', views.update_deposit, name='update_deposit'),
    path('delete/<int:pk>/', views.delete_deposit, name='delete_deposit'),
]