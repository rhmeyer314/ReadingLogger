from django.urls import path
from . import views


urlpatterns = [
    path('get_value/', views.get_values, name='get_values'),
    path('search/', views.search, name='search'),
    path('success/', views.success, name='success'),
    path('users_books/', views.users_books, name='users_books'),
    path('', views.index, name='index'),
]