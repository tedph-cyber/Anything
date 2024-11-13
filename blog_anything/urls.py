from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<slug:section_slug>/", views.post_list, name="post_list"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
]
