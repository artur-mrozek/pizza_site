from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=25)
    password = forms.CharField(label='Hasło', max_length=25, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(label='Login', max_length=25)
    email = forms.EmailField(label="Email", max_length=25)
    password = forms.CharField(label='Hasło', max_length=25, widget=forms.PasswordInput())

class AddressForm(forms.Form):
    address = forms.CharField(label='Adres', max_length=100, widget=forms.Textarea)