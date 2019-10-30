from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*arg,**kwargs):
	print(request.user)
	return render(request,'home.html',{})

def about_view(request,*arg,**kwargs):
	my_context = {
		'my_text': 'This is shahiq',
		'my_number': '123421',
		'my_list': [1,2,3,4,5,6,7]
	} 
	return render(request,'about.html',my_context)