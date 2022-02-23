from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Return a form for comment
    This form will be used in posts detail view
    """
    class Meta:
        model = Comment
        fields = ('name', 'email', 'title', 'message')
