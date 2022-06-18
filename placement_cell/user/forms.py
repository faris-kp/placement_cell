from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class UserRegisterForm(UserCreationForm):

    email=forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email','password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model=User
        fields =['username','email','password1','password2']
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exist")
        return email


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username','password']








