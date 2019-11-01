from django.http import HttpResponse
from django.shortcuts import render
from .models import products
from .forms import productForm,productRawForm

# Create your views here.
#Django Model Forms
def products_create_view(request):
	form = productForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
	'form':form
	}
	return render(request,'products/product_create.html',context)

# Raw HTML form

# def products_create_view(request):
# 	if request.method == 'POST':
# 		title = request.POST.get('title')
# 		description = request.POST.get('description')
# 		summary = request.POST.get('summary')
# 		price = request.POST.get('price')
# 		print(title)
# 		products.objects.create(title=title,description=description,summary=summary,price=price)
# 		# return http.HttpResponseRedirect('/add-products')
# 		# products.objects.create
# 	context = {}
# 	return render(request,'products/product_create.html',context)

#Pure Django Form

# def products_create_view(request):
# 	form = productRawForm()
# 	if request.method == 'POST':
# 		form = productRawForm(request.POST)
# 		if form.is_valid():
# 			print(form.cleaned_data)
# 			products.objects.create(**form.cleaned_data)
# 	context = {
# 		'form': form
# 	}
# 	return render(request,'products/product_create.html',context)
def products_view_page(request):
	product = products.objects.all()
	context = {
	'product':product
	}
	return render(request,'products/product_detail.html',context)