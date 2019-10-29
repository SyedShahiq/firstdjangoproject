from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*arg,**kwargs):
	return HttpResponse('<h1>Hello World</h1>')

def about_view(*arg,**kwargs):
	return HttpResponse('<h1>About us Page</h1>')