from django.shortcuts import render
from django.views.generic import TemplateView
from articles.models import *

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.filter(title__contains = "2")
        return context
    