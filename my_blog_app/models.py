from django.db import models


class Topic(models.Model):
    """Topic model."""
    name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class TopicInfo(models.Model):
    """Information about some topic"""
    topic = models.ForeignKey(Topic, models.CASCADE)
    name = models.CharField(max_length=250)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.text[:30]}"
