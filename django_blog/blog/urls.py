from django.urls import path
from django.contrib.auth import views as auth_views   # django in built auth 


urlpatterns = [
    path('/login/', auth_views.LoginView.as_view(template_name='blog/login.html', name='login')),
    path('/logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html', name='logout'))
]