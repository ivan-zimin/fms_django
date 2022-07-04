from django.shortcuts import render


def lathe_machine(request):
    return render(request, 'lathe_machine/index.html')