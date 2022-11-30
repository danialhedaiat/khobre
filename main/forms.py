from django import forms

from main.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, required=True, widget=forms.TextInput(
        attrs={"class": "username-input", "placeholder": "نام کاربری", "type": "text", "name": "username"}))
    password = forms.CharField(max_length=200, required=True, widget=forms.TextInput(
        attrs={"class": "password-input", "placeholder": "رمز عبور", "type": "password", "name": "password"}))


class CreateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True,
                                widget=forms.TextInput(attrs={"class": "form-control", "name": "first_name"}))
    last_name = forms.CharField(max_length=50, required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "name": "last_name"}))
    username = forms.CharField(max_length=50, required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "name": "username"}))
    phone = forms.CharField(max_length=10, required=True,
                            widget=forms.TextInput(attrs={"class": "form-control", "name": "phone"}))
    address = forms.CharField(max_length=500,
                              widget=forms.TextInput(attrs={"class": "form-control", "name": "address"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'address', 'birthday']

