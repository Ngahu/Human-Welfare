from django.shortcuts import render


def index(request):
    return render(request, 'Welfare/about-us.html')
