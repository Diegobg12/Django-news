from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from datetime import datetime
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail',args=([str(self.id)]))
 

class Article(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='images/', null=True, default="/images/default-image.jpg")
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True, default='2')
    # tags = models.ManyToManyField(Tag)
    tags = TaggableManager()
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
    def date_format(self):
        return self.date.strftime('%b %e %Y & %H ')


# class Replay(models.Model):
#     coment = models.ForeignKey(Comment, 
#     on_delete = models.CASCADE,
#     related_name = 'replies')
#     author = models.ForeignKey(
#         get_user_model(),
#         on_delete = models.CASCADE,
#         # Query the comments related to each author
#     )
#     date = models.DateTimeField(auto_now_add = True)
#     reply = models.CharField(max_length = 140)    
#     def __str__(self):
#         return self.reply
#     def get_absolute_url(self):
#         return reverse('article_list')    

# class Tag(models.Model):
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=200, unique=True)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("posts:tag_index", kwargs={"slug": self.slug})

#     class Meta:
#         ordering = ["-timestamp"]