from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView 
# SignUpView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', list_books, name='books'),
    path('library-details/', LibraryDetailView.as_view(), name='library-details'),
    # path('register/', SignUpView.as_view(), name='register'),
    path('register/', views.register, name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_view, name='admin-dashboard'),
    path('member-dashboard/', views.member_view, name='member-dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-dashboard'),
    path('books/add/', views.add_book, name='add-book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit-book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete-book'),

]