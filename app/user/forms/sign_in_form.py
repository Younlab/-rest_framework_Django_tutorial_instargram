from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
        widgets = {
            'password': forms.PasswordInput()
        }

    def sign_in(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        return user