from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='accounts/login/')
def index(request):
	return render(request, 'cumpa/index.html')


def login(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login_user(request, user)
			return redirect('index')
		else:
			return redirect('login')
	else:
		if not request.user.is_authenticated:
			return render(request, 'session/login.html')
		else:
			return redirect('index')


@login_required(login_url='accounts/login/')
def logout(request):
	logout_user(request)
	return redirect('login')


def chat_robot(request):
	return render(request, 'cumpa/chat_robot.html')

def chat_people(request):
	return render(request, 'cumpa/chat_people.html')

