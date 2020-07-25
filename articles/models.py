from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from datetime import datetime

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def body_into(self):
        return self.body[:100]

    def date_format(self):
        return self.date.strftime('%b %e %Y')
    
    def get_absolute_url(self):
        return reverse('article_detail',args=([str(self.id)]))


class Comment(models.Model):
    article = models.ForeignKey(Article, 
    on_delete = models.CASCADE,
    related_name = 'comments')
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        # Query the comments related to each author
    )
    date = models.DateTimeField(auto_now_add = True)
    comment = models.CharField(max_length = 140)    
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('article_list')    
