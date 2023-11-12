from django import forms

from .models import Post
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    title = forms.CharField(label="Заголовок", widget=forms.TextInput(attrs={'placeholder': 'Введіть заголовок...', 
                                                                            'class' : 'title-input'}))
    text = forms.CharField(label="Текст", widget=forms.Textarea(attrs={'placeholder': 'Введіть текст...',
                                                                        'class' : 'text-input'}))
    image = forms.ImageField(label="Зображення", widget=forms.ClearableFileInput(attrs={'multiple': False}), required=False)

    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)


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


