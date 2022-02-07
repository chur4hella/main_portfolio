from django import forms
from django.forms import ModelForm, modelform_factory, widgets
from .models import Ad, Category, Region, Image
from django.contrib.auth.models import User



class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['type_ad', 'title', 'short_description', 'description', 'price', 'bargain']


AdFormSet = modelform_factory(
    Ad, AdForm,
    widgets={'type_ad': widgets.RadioSelect()}
)


class ImageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({'multiple': True})

    class Meta:
        model = Image
        fields = ['photo']


class FilterForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['type_ad', 'bargain']


FilterFormSet = modelform_factory(
    Ad, FilterForm,
    widgets={'type_ad': widgets.CheckboxSelectMultiple}
)


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name']
        widgets = {
            'password': widgets.PasswordInput()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


# class ProfileForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'email']