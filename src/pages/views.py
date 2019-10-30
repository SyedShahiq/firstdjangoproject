from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*arg,**kwargs):
	return render(request,'home.html',{})

def about_view(request,*arg,**kwargs):
	return render(request,'about.html',{})