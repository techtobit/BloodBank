from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from .froms import DonatorRegistationForm, DonatorProfileUpdateForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
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


# ================== LogOut Profile ===============
class DonatorLogOutView(LogoutView):
	def get_success_url(self):
		if self.request.user.is_authenticated:
			logout(self.request)
		return reversed_lazy('home')


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
	form_class=DonatorProfileUpdateForm
	success_url='profile/'

	def form_valid(self, form):
		user = form.save()
		# after reg user login automaticly 
		login(self.request, user)
		return super().form_valid(form)


