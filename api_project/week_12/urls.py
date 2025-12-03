from django.urls import path, include
from .views import BookListCreateAPIView, BookViewSet
from rest_framework.routers import DefaultRouter

'''
DefaultRouter: Creates standard API root view and generates URLs for ViewSet actions.
SimpleRouter: Similar to DefaultRouter but without the API root view, suitable for simpler APIs.
Custom Routers: Allows you to define custom routing logic for more complex API structures.
'''
router = DefaultRouter()
router.register(r'my-models', BookViewSet)

urlpatterns = [
    path("api/books", BookListCreateAPIView.as_view(), name="book_list_create"),
    path("api/", include(router.urls))
]