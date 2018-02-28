from django.shortcuts import render

def index(request):
    return render(request, 'fertilizing/index.html')

def newFert(request):
    return render(request, 'fertilizing/newFert.html')