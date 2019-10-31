from django.http import HttpResponse
from django.shortcuts import render
from .models import products

# Create your views here.
def products_view_page(request):
	product = products.objects.get(id=1)
	context = {
		'title':product.title,
		'description': product.description
	}
	return render(request,'products/detail.html',context)