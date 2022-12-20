from django import forms

from .models import Topic, TopicInfo


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']


class TopicInfoForm(forms.ModelForm):
    class Meta:
        model = TopicInfo
        fields = ['name', 'text']
