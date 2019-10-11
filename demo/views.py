from django.shortcuts import render

def demoView(request):
    return render(request, 'demo.html')