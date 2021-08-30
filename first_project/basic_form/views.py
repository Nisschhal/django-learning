from django.shortcuts import render
from .forms import NewForm, UserForm, UserProfileInfoForm

# for login and logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def basic_form_index(request):
	form = NewForm
	if request.method == 'POST':
		form = NewForm(request.POST)
		if form.is_valid():
			print('Name: ', form.cleaned_data['name'])
			print('Email: ', form.cleaned_data['email'])
			print('Text: ', form.cleaned_data['text'])
	return render(request, 'basic_form/basic_form_index.html', {'form': form})


def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileInfoForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)  # getting input password and hashing
			user.save()  # saving the hashed password

			profile = profile_form.save(commit=False)
			profile.user = user  # linking this profile to that user from form

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm
		profile_form = UserProfileInfoForm

	return render(request, 'basic_form/registration.html', {
		'user_form': user_form,
		'profile_form': profile_form,
		'registered': registered
	})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('/'))
			else:
				return HttpResponse('Account is not active!!')
		else:
			print('not a user !!')
			return HttpResponse('Invalid login details ')
	else:
		return render(request, 'basic_form/login.html')


@login_required
def special(request):
	return HttpResponse('Welcome, you are logged in')


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('/'))
