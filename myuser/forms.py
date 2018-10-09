from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationform(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationform, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', })
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', })
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', })
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', })

    email = forms.EmailField()

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password1', "password2"]

        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'password1': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'password2': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #     }),
        # }
