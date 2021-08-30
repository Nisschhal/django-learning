from first_app import views
from django.urls import path

urlpatterns = [
	path('', views.first_app_index),
	path('acc_records/', views.acc_records),

]
