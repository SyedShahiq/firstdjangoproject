from django import forms
from .models import products
#Django Model Form
class productForm(forms.ModelForm):
	title       = forms.CharField(label='Title')
	summary     = forms.CharField(widget=forms.Textarea({
		'placeholder':'Summarys',
		'class': 'form-group'
		}))
	class Meta:
		model = products
		fields = [
			'title',
			'description',
			'price',
			'summary',
			'featured'
		]
	# def clean_title(self,*args,**kwargs):
	# 	title = self.cleaned_data.get("title")
	# 	if "abc" in title:
	# 		return title
	# 	else:
	# 		raise forms.ValidationError('This is not a valid title')

#Pure Django Form
class productRawForm(forms.Form):
	title       = forms.CharField(label='Title')
	price       = forms.DecimalField()
	summary     = forms.CharField(widget=forms.Textarea({
		'placeholder':'Summary',
		'class': 'abc'
		}))
	description = forms.CharField(required=False)