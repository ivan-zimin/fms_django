from django.shortcuts import render

def milling_machine(request):
    return render(request, 'milling_machine/index.html')