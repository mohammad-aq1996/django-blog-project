from django import forms
from .models import Comment, Post
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    """
    Return a form for comment
    This form will be used in posts detail view
    """

    class Meta:
        model = Comment
        fields = ('name', 'email', 'title', 'message')


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('author', 'title', 'content', 'image', 'category', 'tags')
