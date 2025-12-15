from rest_framework import serializers
from .models import BlogPost, Comment, User


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)  # customizing serializers

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'author_name', 'created_at']


# serializers validation
class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)    # nested serializer for related objects
    class Meta:
        model = BlogPost
        fields = ['id', 'content', 'author', 'title', 'created_at']


    def validate(self,date):
        if len(data['title']) < 5:
            raise serializers.ValidationError('Title must be at least 5 characters')
        return data
    
class User(serializers.ModelSerializers):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ['full_name', 'first_name', 'last_name']