from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        # opttionally accept a user instance when initializing the form

        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        post = super().save(commit=False)
        if self.user and not post.author_id:  # only set if not already set
            post.author = self.user
        if commit:
            post.save()
        return post


class PostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author', 'post']