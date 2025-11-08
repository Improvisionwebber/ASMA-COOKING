# asma_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    gallery_images = Product.objects.exclude(id__isnull=True)
    return render(request, 'home.html', {'gallery_images': gallery_images})



def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    # optional: get 5 related products (excluding this one)
    related = Product.objects.exclude(id=id)[:5]
    return render(request, 'product_detail.html', {
        'product': product,
        'related': related
    })