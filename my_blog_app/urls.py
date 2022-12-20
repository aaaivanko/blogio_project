from django.urls import path

from . import views

app_name = 'my_blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic_info, name='topic_info'),
    path('topics/new_topic/', views.new_topic, name='new_topic'),
    path('new_topic_info/<int:topic_id>/', views.new_topic_info, name='new_topic_info'),
]
