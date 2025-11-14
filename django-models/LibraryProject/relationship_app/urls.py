from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_all_books, name='books'),
    path('library-details/', views.display_library_details.as_view(), name='library-details'),
]