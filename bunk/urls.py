from django.urls import path
from django.contrib.auth.views import LogoutView


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/<int:pk>", views.personalBunk, name="user"),
    path("bunk/<int:pk>", views.detail, name="detail"),
    path("bunker", views.bunker, name="bunker"),
    path("bunker_submit", views.bunkerSubmit, name="bunker_submit"),
    path('logout/', LogoutView.as_view(template_name='reguistration/logout.html')), 
    path("signup", views.signup, name="signup"),
    path("signup_submit", views.signup_submit, name="signup_submit"),
] 