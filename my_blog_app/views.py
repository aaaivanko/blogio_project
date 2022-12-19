from django.shortcuts import render

from .models import Topic, TopicInfo


def home(request):
    """Home page!"""
    return render(request, 'my_blog_app/home.html')


def topics(request):
    all_topics = Topic.objects.order_by('date_created')
    context = {'all_topics': all_topics, 'title': 'List of topics!'}
    return render(request, 'my_blog_app/topics.html', context)


def topic_info(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic_infos = topic.topicinfo_set.order_by('-date_added')
    context = {'topic': topic, 'topic_infos': topic_infos, 'title': 'Topic infos'}
    return render(request, 'my_blog_app/topic_info.html', context)


def empty_view(request):
    pass
