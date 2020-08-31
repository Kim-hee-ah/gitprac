from django.shortcuts import render, request

def home(request):


    return render(request, 'home.html', context)

# Create your views here.
