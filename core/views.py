from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def morocco_view(request):
    return render(request, 'morocco.html')

def about_view(request):
    return render(request, 'about.html')

def culture_view(request):
    return render(request, 'culture.html')

def holidays_view(request):
    return render(request, 'holidays.html')

def family_view(request):
    return render(request, 'family.html')

def contact_view(request):
    return render(request, 'contact.html')