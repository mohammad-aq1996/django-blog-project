from django import forms
from . models import Comment


class CommentForm(forms.ModelForm):
    # Return a form for comment
    class Meta:
        model = Comment
        fields = ('name', 'email', 'subject', 'message')
