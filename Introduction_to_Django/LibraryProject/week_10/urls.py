from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('hello/', views.hello_view, name='hello'), 
    path('about/', views.AboutView.as_view(), name='about'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='week_10/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='week_10/logout.html'), name='logout'), 
]