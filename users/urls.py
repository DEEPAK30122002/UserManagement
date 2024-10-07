from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create_or_update, name='user_create'),
    path('edit/<int:id>/', views.user_create_or_update, name='user_update'),
    path('delete/<int:id>/', views.user_delete, name='user_delete'),
]