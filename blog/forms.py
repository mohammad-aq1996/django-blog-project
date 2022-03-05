from django import forms
from .models import Comment, Post, Tag, Category
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


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

        fields = ('author', 'title', 'content', 'created_at', 'published_at', 'image', 'category', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),
            'category': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['created_at'] = JalaliDateField(label='تاریخ ایجاد', widget=AdminJalaliDateWidget)
        self.fields['published_at'] = JalaliDateField(label='تاریخ انتشار', widget=AdminJalaliDateWidget)


