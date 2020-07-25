from django.contrib import admin
from .models import *

# SHOW THE COMMENTS INSIDE THE ARTICLES IN THE ADMIN
# 1ST OPTION: StackedInline 
# 2TH OPTION: TabularInline
class ComentInline(admin.TabularInline):
    model = Comment
    # No Fields by default
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    # Show the comments inside every article
    inlines = [ComentInline,]

# class CustomComment(Comment):
#     model = Comment
#     list_display = ['date', 'comment']

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
