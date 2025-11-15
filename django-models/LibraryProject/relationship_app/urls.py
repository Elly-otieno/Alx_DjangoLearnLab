from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, SignUpView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', list_books, name='books'),
    path('library-details/', LibraryDetailView.as_view(), name='library-details'),
    # path('register/', SignUpView.as_view(), name='register'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]