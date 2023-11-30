from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('input/', views.input, name='input'),
    path('interview/', views.interview, name='interview'),
    path('student/<int:pk>/', views.bio, name='student')
]
