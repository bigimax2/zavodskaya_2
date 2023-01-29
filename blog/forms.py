from django.forms import ModelForm
from django import forms

from blog.models import Post


class AllPosts(ModelForm):
    class Meta:
        model = Post(id_post='get_post')
        fields = '__all__'


class NewPost(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
