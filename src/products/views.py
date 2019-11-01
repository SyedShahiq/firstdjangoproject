from django.http import HttpResponse
from django.shortcuts import render
from .models import products

# Create your views here.
def products_view_page(request):
	product = products.objects.all()
	context = {
	'product':product
	}
	return render(request,'products/product_detail.html',context)