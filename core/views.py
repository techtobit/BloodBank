from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
	data = {' Name' : 'Ashraf Uddin'}
	return render(request, 'home.html', data)