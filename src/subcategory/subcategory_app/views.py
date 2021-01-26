from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Subcategory, Product


def index(request):
    category = Category.objects.all()
    subtegory = Subcategory.objects.all()
    product = Product.objects.all()
    context = {
        'categories': category,
        'subcategories': subtegory,
        'products': product
    }
    return render(request, 'subcategory_app/index.html', context)
