from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


# from django.core import validators


# Create your models here.
def start_with_n(value):
	if value[0].lower() != 'n':
		raise forms.ValidationError('Name must start with n')


class NewForm(forms.Form):
	name = forms.CharField(max_length=200, validators=[start_with_n])
	email = forms.EmailField()
	verify_email = forms.EmailField(label="Enter your enter again")
	text = forms.CharField(widget=forms.Textarea)
	bot_catcher = forms.CharField(widget=forms.HiddenInput, required=False)

	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']
		if email != vmail:
			raise forms.ValidationError('Emails are not matched!!')


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = 'username', 'email', 'password'


class UserProfileInfoForm(forms.ModelForm):
	class Meta:
		model = UserProfileInfo
		fields = ('portfolio_site', 'profile_pic')
