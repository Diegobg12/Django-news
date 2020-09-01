from django.contrib import admin
import django.contrib.admin.options as admin_opt
from .models import *

# SHOW THE COMMENTS INSIDE THE ARTICLES IN THE ADMIN
# 1ST OPTION: StackedInline 
# 2TH OPTION: TabularInline
def dup_event(modeladmin:admin_opt.ModelAdmin, request, queryset):
    for object in queryset:
        from_id = object.id
        object.id = None
        object.save()
        message="dup from {} to {}".format(from_id, object.id)
        modeladmin.log_addition(request=request,object=object,message=message)

dup_event.short_description = "Duplicate Records"

class ComentInline(admin.TabularInline):
    model = Comment
    # No Fields by default
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    # Show the comments inside every article
    inlines = [ComentInline]
    actions = [dup_event]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Category)
# admin.site.register(Tag)

# admin.site.register(Replay)
