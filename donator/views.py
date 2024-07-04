from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .froms import DonatorRegistationForm, DonatorProfileUpdateForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView

# ================== Registation ===============
# Create your views here.
# def DonatorRegistationView(request):
# 	if request.method == 'POST':
# 		form = DonatorRegistationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		form = DonatorRegistationForm()
# 	return render(request, 'donatorResgistation.html', {"form":form})
	

	# ---------Class Base ------------
class DonatorRegistationView(FormView):
	template_name='donatorResgistation.html'
	form_class=DonatorRegistationForm
	success_url='/'

	def form_valid(self, form):
		user = form.save()
		# after reg user login automaticly 
		login(self.request, user)
		return super().form_valid(form)

# ================== LogIN Account ===============
# def DonatorLogInView(request):
# 	username=request.POST.get('username')
# 	password=request.POST.get('password')
# 	user=authenticate(request, username=username, password=password)
# 	if user is not None:
# 		login(request, user)
# 		return HttpResponseRedirect('profile/')
# 	else:
# 		print('error: user id or pass invalied')

class DonatorLogInView(LoginView):
	template_name ='donatorLogIn.html'
	def get_success_url(self):
		return reverse_lazy('profile')


# ================== LogOut Profile ===============
class DonatorLogOutView(LogoutView):
	def get_success_url(self):
		if self.request.user.is_authenticated:
			logout(self.request)
		return reverse_lazy('home')


# ================== Update Profile ===============

# def DonatorProfileUpdateView(request):
# 	if request.method == 'POST':
# 		form = DonatorProfileUpdateForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		form = DonatorProfileUpdateForm()
# 	return render(request, 'donatorProfileUpdate.html', {"form":form})


	# ---------Class Base ------------
class DonatorProfileUpdateView(FormView):
	template_name='donatorProfileUpdate.html'

	def get(self, request):
		form = DonatorProfileUpdateForm(instance=request.user)
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = DonatorProfileUpdateForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
		return render(request, self.template_name, {"form":form})

