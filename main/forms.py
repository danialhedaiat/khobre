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
    phone = forms.CharField(max_length=11, required=True,
                            widget=forms.TextInput(
                                attrs={"class": "form-control", "name": "phone", "onkeyup": "phoneNumberCheck(this)"}))
    address = forms.CharField(max_length=500, required=False,
                              widget=forms.Textarea(attrs={"class": "form-control", "name": "address", "rows": "3"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'address', 'birthday', 'username']
