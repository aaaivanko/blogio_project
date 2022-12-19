from django.shortcuts import render


def home(request):
    """Home page!"""
    return render(request, 'my_blog_app/home.html')
