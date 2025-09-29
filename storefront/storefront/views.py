from django.shortcuts import render

def index(request):
    return render(request, 'storefront/store.html', {'name': 'Store User'})

def store(request):
    return render(request, "storefront/store.html")

def home(request):
    return render(request, "storefront/home.html")