from django.http import HttpResponse
from django.shortcuts import render
from static.primarchs_data import primarchs_data

def main_page(request):
    primarch = primarchs_data()

    return render(request, 'main_page.html', {'primarch': primarch})