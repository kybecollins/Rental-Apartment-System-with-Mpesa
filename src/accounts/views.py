from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm, AccountAuthenticationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def signup_view(request):
    # context={}
    # form = UserCreationForm()
    # context['form'] = form
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return render(request,'accounts/login.html')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/signup.html', context)



def logout_view(request):
	logout(request)
	return redirect('home')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("dashboards:homedash")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("dashboards:homedash")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "accounts/login.html", context)

def home_view(request):
    context={}
    return render(request,'accounts/index.html',context)
