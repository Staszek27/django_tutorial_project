from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_detail_view(request):
    context = {
        'object' : Product.objects.get(id = 1)
    }
    return render(request, 'product/product_detail.html', context)



def product_create_view(request):
    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            
    context = {
        'form' : form
    }
    return render(request, 'product/product_create.html', context)