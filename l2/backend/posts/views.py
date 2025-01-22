from django.shortcuts import render


def postList(request):
    return render(request, "posts/posts_list.html")


# Create your views here.
