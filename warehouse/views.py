from django.shortcuts import render

def warehouse_page(request):
    return render(request, 'warehouse/warehouse_page.html')