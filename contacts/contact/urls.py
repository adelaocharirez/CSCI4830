from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:id>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
    path('search/', views.search_contact, name='search_contact'),
]
