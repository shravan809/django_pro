from django.urls import path
from . import views

urlpatterns = [
    path('', views.slide),
    path('slide',views.slide2)
]