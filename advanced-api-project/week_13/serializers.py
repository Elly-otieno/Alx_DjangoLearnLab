from rest_framework import serializers
from .models import BlogPost, Comment, User

class User(serializers.ModelSerializers):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ['full_name', 'first_name', 'last_name']


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)  # customizing serializers

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'author_name', 'created_at']


# serializers validation
class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)    # nested serializer for related objects
    class Meta:
        model = BlogPost
        fields = ['id', 'content', 'author', 'title', 'created_at', 'comments', 'likes']
        read_only_fields = ['created_at', 'likes']


    # def validate(self, data):
    #     if len(data['title']) < 5:
    #         raise serializers.ValidationError('Title must be at least 5 characters')
    #     return data
    '''
    Implement validation to ensure the comment author is the same as the blog post author.
    '''

    def validate(self,data):
        blog_author = data.get('author')
        comments = self.initial_data.get('comments', [])

        for comment in comments:
            if int(comment['author']) != blog_author.id:
                raise serializers.ValidationError('Each comment author must be the same as blog post author')
            return data
        
    '''
    Modify the BlogPostSerializer to allow creating and updating blog posts with related comments
    '''
    def create(self, validated_data):
        comments_data = validated_data.pop('comments', [])
        blog_post = BlogPost.objects.create(**validated_data)
        for comment_data in comments_data:
            Comment.objects.create(blog_post=blog_post, **comment_data)
        return blog_post
    

    def update(self, instance, validated_data):
        comments_data = validated_data.pop('comment', [])

        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()

        if comments_data is not None:
            instance.comments.all().delete()  # delete all the commments
            for comment_data in comments_data:
                Comment.objects.create(blog_post=instance, **comment_data)   # recreate comments

        return instance
    
    '''
             instead of deleting all comments and recreating them, we update them in place. 
             This way, existing comments keep their IDs and timestamps, and only the changed fields are updated
            '''
        # if comments_data is not None:
        #     for comment_data in comments_data:
        #         # Try to find an existing comment by ID
        #         comment_id = comment_data.get('id', None)
        #         if comment_id:
        #             try:
        #                 comment = instance.comments.get(id=comment_id)
        #                 # Update existing comment fields
        #                 comment.title = comment_data.get('title', comment.title)
        #                 comment.content = comment_data.get('content', comment.content)
        #                 comment.author = comment_data.get('author', comment.author)
        #                 comment.save()
        #             except Comment.DoesNotExist:
        #                 # If not found, create a new comment
        #                 Comment.objects.create(blog_post=instance, **comment_data)
        #         else:
        #             # If no ID provided, create a new comment
        #             Comment.objects.create(blog_post=instance, **comment_data)

        # return instance

