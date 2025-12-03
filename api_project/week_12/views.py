from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset
        #queryset = super().get_queryset()
        title_filter = self.request.query_params.get('title', None)
        if title_filter is not None:
            queryset = queryset.filter(title__icontains=title_filter)  
        return queryset


'''
VIEWSETS - 
Provides high level abstraction for creating API views that handle common CRUD operations on models
ViewSets group these actions (e.g., list, retrieve, create, update, delete) together, reducing code duplication and promoting consistency.

ModelViewSet: Provides a complete set of CRUD operations for a model, including list, retrieve, create, update, and delete actions.
ReadOnlyModelViewSet: Offers read-only operations, such as list and retrieve, suitable for exposing data without allowing modifications.
ViewSet: A base class that allows you to define custom actions and implement specific API behavior.
'''

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Authentication and permissions

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

class MyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only authenticated users can access this view
        #return Response({'message': 'Hello, authenticated user!'})
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
    
class MyAPICreateView(APIView):
    authrntication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        # Only admins can create a new model instances
        serializer = BookSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)