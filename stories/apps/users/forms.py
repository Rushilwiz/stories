from allauth.account.forms import SignupForm
from django.contrib.auth import forms as admin_forms
from django.utils.translation import gettext_lazy as _

from django import forms

from .models import User

class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):  # type: ignore[name-defined]
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):  # type: ignore[name-defined]
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """
    full_name = forms.CharField(max_length=255, label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))

    def save(self, request):
        user = super(UserSignupForm, self).save(request)
        user.full_name = self.cleaned_data['full_name']
        user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image', 'cropping', 'full_name']