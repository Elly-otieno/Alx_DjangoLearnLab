from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'), 
    path('about/', views.AboutView.as_view(), name='about'), 
]