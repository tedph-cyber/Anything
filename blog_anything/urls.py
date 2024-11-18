from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.home, name="home"),
    path("<slug:section_slug>/", views.post_list, name="post_list"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
=======
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('sections/', views.section_list, name='section_list'),
    path('post/<slug:section_slug>/', views.post_list, name='post_list'),
    path('post/<slug:section_slug>/<uuid:post_uuid>/', views.post_detail, name='post_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
>>>>>>> features/authentication
]
