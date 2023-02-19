from django import forms

from .models import Post
from .models import Comment


class PostForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)
        my_image = forms.ImageField()



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)