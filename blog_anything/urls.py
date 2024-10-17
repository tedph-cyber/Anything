from django.urls import path
from . import views

urlpatterns = [
    path('', views.section_list, name='section_list'),
    path('<slug:section_slug>/', views.post_list, name='post_list'),
]
