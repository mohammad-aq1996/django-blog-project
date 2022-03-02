from django import forms
from .models import Comment, Post, Tag, Category
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User


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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),
            'category': forms.RadioSelect(),
        }
        # category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.C)
        # tags = forms.ModelMultipleChoiceField(
        #     queryset=Tag.objects.all(),
        #     widget=forms.widgets.CheckboxSelectMultiple()
        # )
        #