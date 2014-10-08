from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	return render(request, 'dashboard/index.html')

def apiRedirect(request):
	return redirect('/api/get')

def loginRedirect(request):
	return redirect('/admin/')
