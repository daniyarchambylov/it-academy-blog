from django.shortcuts import render


def list_categories(request):
    return render(request, 'categories/list.html')
