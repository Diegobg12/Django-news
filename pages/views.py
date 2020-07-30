from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from articles.models import *


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        allPublished = Article.objects.order_by('date').all()
        context['lastPost'] = allPublished[0]
        context['frontPosts'] = allPublished[1:3]
        context['middle'] = allPublished[4]
        context['restPost'] = allPublished[5:]
        context['mostPopular'] = allPublished[0:5]
        
        return context
    
class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'


class SearchResultsView(ListView):
    model = Article
    template_name = 'search.html'
    context_object_name = 'search_results'

    def get_queryset(self):
       result = super(SearchResultsView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Article.objects.filter(body__contains=query)
          result = postresult
       else:
           result = None
       return result
    
    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['search_value'] = self.request.GET.get('search')
        return context
    