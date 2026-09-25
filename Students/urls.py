

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path("home/", views.home, name="home"),
    path('admission/', views.admission_form, name='admission_form'),
    path("Students/", views.stu_details, name="stu_details"),
    path("logout/", views.logout_view, name="logout"),
    path(
    "delete/<int:id>/",
    views.delete_student,
    name="delete_student"
),
]