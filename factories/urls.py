from django.urls import path
from factories import views


app_name = 'factories'


urlpatterns = [
    path('add/', views.add_factory, name='add_factory'),
    path('update/<int:pk>/', views.update_factory, name='update_factory'),
    path('delete/<int:pk>/', views.delete_factory, name='delete_factory'),
]