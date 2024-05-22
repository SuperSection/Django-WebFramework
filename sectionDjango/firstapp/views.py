from django.shortcuts import render

# Create your views here.
def new_app(request):
    return render(request,'firstapp/new_app.html',context=None)