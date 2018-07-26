from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

User = get_user_model()

class SignUpForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='비밀번호 확인',
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password2',
            'first_name',
            'last_name',
            'email',
            'site',
            'profile_image',
        )
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)

        if user.exists():
            raise ValidationError('중복된 ID 입니다.')
        else:
            return username

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            self.add_error('password2', '비밀번호가 일치하지 않습니다.')
        else:
            return self.cleaned_data

    def created_user(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            site=self.cleaned_data['site'],
            profile_image=self.cleaned_data['profile_image'],
        )

        return user
