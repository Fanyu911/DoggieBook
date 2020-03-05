from django import forms
from doggie.models import DogCategory, Dog, UserProfile
from django.contrib.auth.models import User

class DogCategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Please enter the Dogcategory name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
    # an association
        model = DogCategory
        fields = ('name',)


class DogForm(forms.ModelForm):
    dogcategory = forms.ModelChoiceField(queryset=DogCategory.objects.all(), empty_label="Choose category",help_text="Select.")
    dog_name = forms.CharField(max_length=128,help_text="Please enter the name of the dog.")
    short_description = forms.CharField(max_length=1280, help_text="Please enter the short description of the dog.")
    long_description = forms.CharField(max_length=1280, help_text="Please enter the long description of the dog.")
    price = forms.IntegerField(max_value=10000, help_text="Please enter the price of the dog.")
    life_span = forms.CharField(max_length=1280, help_text="Please enter the life span of the dog.")

    class Meta:
        model = Dog
        exclude = ('likes','dogcategory_slug','views','slug')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user','picture',)
