from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import BlogPostSerializer
from .models import BlogPost

from rest_framework import mixins, generics


# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    @action(detail=True, method=['post'])
    def like(self, request, pk=None):
        '''
        Custom action to 'like' a blog post.
        
        :param self: Description
        :param request: Description
        :param pk: Description
        '''

        blog_post = self.get_object()
        blog_post.likes += 1
        blog_post.save()
        serializer = self.get_serializer(blog_post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BlogPostListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    '''
    Custom views with DRF generics and mixins
    '''
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get(self, request, *args, **kwargs):
        # Handles GET requests (list all blog posts)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handles POST requests (create a new blog post)
        return self.create(request, *args, **kwargs)


class BlogPostDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    
    '''
    Customizing Behavior
    '''
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get(self, request, *args, **kwargs):
        # GET /blogposts/{id}/ → retrieve single post
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # PUT /blogposts/{id}/ → update post
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # DELETE /blogposts/{id}/ → delete post
        return self.destroy(request, *args, **kwargs)
    
'''
Using Concrete Generic Views 
Instead of writing mixins manually, DRF provides ready-made classes
'''
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


