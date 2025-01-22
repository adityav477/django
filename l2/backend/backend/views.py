# from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    # return HttpResponse("Hello from homePage")
    return render(request, "home.html")


def aboutPage(request):
    # return HttpResponse("Hello from About Page")
    return render(request, "about.html")
