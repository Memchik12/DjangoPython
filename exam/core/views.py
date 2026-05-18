from django.http import HttpResponse
from django.shortcuts import render
from static.primarchs_data import primarchs_data

def main_page(request):
    primarch = primarchs_data()

    return render(request, 'main_page.html', {'primarch': primarch})

def contact(request):
    return render(request, 'contact.html')
def privacy(request):
    return render(request, 'privacy.html')
def terms(request):
    return render(request, 'terms.html')