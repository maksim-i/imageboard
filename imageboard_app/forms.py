from django import forms
from .models import Post, Reply

class PostForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ['image', 'subject', 'description']
        labels = {'image': '', 'subject': '', 'description': ''}

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
        labels = {'text': ''}
