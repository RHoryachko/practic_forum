from django import forms

from .models import Post
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)
        my_image = forms.ImageField()



class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'type-comment',
            'id': 'text',
            'placeholder': 'Add comment...'
        }),
        label=''  # Встановлюємо label пустим рядком, щоб забрати атрибут for
    )

    class Meta:
        model = Comment
        fields = ('text',)


