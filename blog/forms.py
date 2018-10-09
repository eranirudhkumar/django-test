from django import forms


class StudentPortalLoginForm(forms.Form):
    uname=forms.CharField(label="User id:",max_length=15)
    uemail=forms.EmailField(label="User Email:")
    pword=forms.CharField(label="Password:",widget=forms.PasswordInput())