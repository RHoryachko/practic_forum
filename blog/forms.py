from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)
        my_image = forms.ImageField()