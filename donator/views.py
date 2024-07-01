from django.http import HttpResponseRedirect
from django.shortcuts import render
from .froms import DonatorRegistationForm

# Create your views here.
def DonatorRegistationView(request):
	if request.method == 'POST':
		form = DonatorRegistationForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('')
	else:
		form = form = DonatorRegistationForm()
	return render(request, 'donatorResgistation.html', {"form":form})



