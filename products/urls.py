from django.urls import path
from products import views


app_name = 'products'


urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    # path('update/<int:pk>/', views.update_product, name='update_product'),
    # path('delete/<int:pk>/', views.delete_product, name='delete_product'),

    path('category/add/', views.add_category, name='add_category'),

]