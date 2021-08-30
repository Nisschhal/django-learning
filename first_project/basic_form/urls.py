from django.urls import path
from . import views

urlpatterns = [
	path('', views.basic_form_index),
	path('register/', views.register),
	path('user_login/', views.user_login),
	path('user_logout/', views.user_logout),



]
