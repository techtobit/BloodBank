from django.http import HttpResponseRedirect
from django.shortcuts import render
from .froms import DonatorRegistationForm, DonatorProfileUpdateForm
from django.views.generic.edit import FormView

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
		form
		return super().form_valid(form)
	



def DonatorProfileUpdateView(request):
	if request.method == 'POST':
		form = DonatorProfileUpdateForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = DonatorProfileUpdateForm()
	return render(request, 'donatorProfileUpdate.html', {"form":form})



