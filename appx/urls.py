from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login_user", views.login_user, name="login"),
    path("dashboard",views.dashboard, name="dashboard"),
]
