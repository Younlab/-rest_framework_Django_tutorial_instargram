from django import forms
from .models import Post


class PostCreate(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput()
    )
    image = forms.ImageField(
        widget=forms.FileInput()
    )

    class Meta:
        model = Post
        fields = (
            'content',
            'image',
        )

    def post_create(self, author):
        return Post.objects.create(
            author=author,
            content=self.cleaned_data['content'],
            image=self.cleaned_data['image'],
        )
