from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.course_list),
    path('<int:pk>/', views.course_detail),
    path('lesson/<int:pk>/', views.lesson_detail),
]