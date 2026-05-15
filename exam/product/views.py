from django.shortcuts import render, get_object_or_404
from .models import Product
products = Product.objects.filter(race_type='space_marine')

def product_list(request):
    products = Product.objects.filter(race_type='space_marine')[:3]

    # Передаем их в шаблон 'product_list.html'
    return render(request, 'product/product_list.html', {'products': products})
def product_detail(request, pk):
    # Ищет товар по ID, если не найдет — выдаст ошибку 404
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'products': products})

def sm_list(request):
    # Берем из базы ТОЛЬКО Космодесант
    products = Product.objects.filter(race_type='space_marine')
    # Указываем путь к новой папке space_marines
    return render(request, 'product/space_marines/sm_list.html', {'products': products})
def sm_details(request, pk):
    # Ищем товар по ID, но ОБЯЗАТЕЛЬНО проверяем, что это Космодесант
    products = get_object_or_404(Product, pk=pk, race_type='space_marines')
    return render(request, 'product/space_marines/sm_details.html', {'product': products})


def imp_details(request, pk):
    products = get_object_or_404(Product, pk=pk, race_type='imperium')
    return render(request, 'product/imperium/imp_details.html', {'product': products})

def imp_list(request):
    products = Product.objects.filter(race_type='imperium')
    return render(request, 'product/imperium/imp_list.html', {'products': products})

def chaos_details(request, pk):
    products = get_object_or_404(Product, pk=pk, race_type='chaos')
    return render(request, 'product/chaos/chaos_details.html', {'product': products})

def chaos_list(request):
    # Берем из базы ТОЛЬКО Космодесант
    products = Product.objects.filter(race_type='chaos')
    return render(request, 'product/chaos/chaos_list.html', {'products': products})

def xenos_details(request, pk):
    products = get_object_or_404(Product, pk=pk, race_type='xenos')
    return render(request, 'product/xenos/xenos_details.html', {'product': products})

def xenos_list(request):
    products = Product.objects.filter(race_type='xenos')
    return render(request, 'product/xenos/xenos_list.html', {'products': products})
