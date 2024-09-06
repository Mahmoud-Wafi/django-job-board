from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import City, Profile
from phonenumber_field.formfields import PhoneNumberField

class SignupForm(UserCreationForm):
    usable_password=None
    phone_number = PhoneNumberField(required=False)
    image = forms.ImageField(required=False)
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False)
    class Meta:
        model = User
        fields = ["username","first_name","last_name", "email", "password1", "password2", "phone_number", "image"]

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Phone Number'})
        self.fields['image'].widget.attrs.update({'placeholder': 'Profile Image'})
        self.fields['city'].widget.attrs.update({'placeholder': 'City'})



class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','phone_number','city']