# from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    # return HttpResponse("Hello World!")
    return render(request, "home.html")


def aboutPage(request):
    # return HttpResponse("Hello From about Page!")
    return render(request, "about.html")
