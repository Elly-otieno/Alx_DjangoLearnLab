from rest_framework import serializers
from .models import Book, Post
from django.utils import timezone

'''
convert complex data structures such as django models into formats like JSON / XML / YAML - hence suitable for consumption
'''

class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['id', 'title', 'author', 'publication_date', 'created_at', 'days_since_created']
    
    def get_days_since_created(self, obj):
        # from datetime import datetime, timezone
        # return (datetime.now(timezone.utc) - obj.created_at).days
        delta = timezone.now() - obj.created_at
        return delta.days
    
    def validate(self, data):
        if len(data['title']) < 5:
            raise serializers.ValidationError("title must be atleast 5 characters long.")
        return data
    

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']