from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'website/index.html')


def about(request):
    # return HttpResponse("Django About page")
    return render(request, 'website/about.html')


def contact(request):
    # return HttpResponse("Django Contact page")
    return render(request, 'website/contact.html')

