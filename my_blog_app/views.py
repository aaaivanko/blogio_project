from django.shortcuts import render

from .models import Topic


def home(request):
    """Home page!"""
    return render(request, 'my_blog_app/home.html')


def topics(request):
    all_topics = Topic.objects.order_by('date_created')
    context = {'all_topics': all_topics, 'title': 'List of topics!'}
    return render(request, 'my_blog_app/topics.html', context)
