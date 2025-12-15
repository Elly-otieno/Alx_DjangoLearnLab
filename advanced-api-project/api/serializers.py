from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

        def validate(self, data):
            current_year = datetime.now.year
            if data['publication_year'] > current_year:
                raise serializers.ValidationError('Pulication year cannot be in the future')
            return data

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) # nested book serializer
    class Meta:
        model = Author
        fields = ['name', 'books']