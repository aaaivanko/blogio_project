from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm


def home(request):
    """Home page!"""
    return render(request, 'my_blog_app/home.html')


def topics(request):
    """Show all topics"""
    all_topics = Topic.objects.order_by('date_created')
    context = {'all_topics': all_topics, 'title': 'List of topics!'}
    return render(request, 'my_blog_app/topics.html', context)


def topic_info(request, topic_id):
    """Show info about particular topic!"""
    topic = Topic.objects.get(id=topic_id)
    topic_infos = topic.topicinfo_set.order_by('-date_added')
    context = {'topic': topic, 'topic_infos': topic_infos, 'title': 'Topic infos'}
    return render(request, 'my_blog_app/topic_info.html', context)


def new_topic(request):
    """Create a new topic."""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_blog:topics')
    context = {'form': form, 'title': 'Create new topic.'}
    return render(request, 'my_blog_app/new_topic.html', context)
