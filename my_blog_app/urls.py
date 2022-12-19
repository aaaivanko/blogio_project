from django.urls import path

from . import views

app_name = 'my_blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic_info, name='topic_info'),

]
