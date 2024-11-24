from django.urls import path
from . import views

urlpatterns = [
    path('', views.policy_list, name='policy_list'),
    path('add/', views.add_policy, name='add_policy'),
    path('edit/<int:pk>/', views.edit_policy, name='edit_policy'),
    path('delete/<int:pk>/', views.delete_policy, name='delete_policy'),
]
