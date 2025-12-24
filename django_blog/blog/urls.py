from django.urls import path
from django.contrib.auth import views as auth_views   # django in built auth 
from .views import SignUpView, PostCreateView, PostDeleteView, PostDetailView, PostDisplayView, PostUpdateView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html', name='login')),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html', name='logout')),
    path('register/', SignUpView.as_view(template_name='blog/register.html', name='register')),
    path('posts/', PostDisplayView.as_view(template_name='blog/posts.html', name='posts')),
    path('post/new/', PostCreateView.as_view(template_name='blog/create_post.html', name='create_post')),
    path('post/<int:pk>/', PostDetailView.as_view(template_name='blog/view_post.html', name='view_post')),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name='blog/edit_post.html', name='edit_post')),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name='blog/delete_post.html', name='delete_post')),
]