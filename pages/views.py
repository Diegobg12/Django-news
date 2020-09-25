from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from articles.models import *
from django.shortcuts import get_object_or_404
from itertools import chain
from taggit.models import Tag
from users.models import *
from django.template import RequestContext
from .forms import *
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.defaults import page_not_found

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

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    # send_mail(ContactForm.send_info(self), 
    # 'message', 
    # 'bygreenxsas@gmail.com', 
    # ['bygreenxsas@gmail.com'], fail_silently=False)

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)


class SearchResultsView(ListView):
    model = Article
    template_name = 'search.html'
    context_object_name = 'search_results'

    def get_queryset(self):
       result = super(SearchResultsView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Article.objects.filter(body__contains=query)
          title = Article.objects.filter(title__contains=query)
          category_id = list(Category.objects.filter(title__contains=query))
          if len(category_id)>0:
              category = Article.objects.filter(category=category_id[0])
              combined_results = list(chain(title, postresult,category))
          else:
              combined_results = list(chain(title, postresult))
        #   combined_results = title | postresult
          result = combined_results 
       else:
           result = None
       return result
    
    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['search_value'] = self.request.GET.get('search')
        return context


class CategoryView(ListView):
    model = Article
    template_name = 'article_category.html'
# Get the category id from the url
    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Article.objects.filter(category=self.category)
# Add the category in our dicctionary
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        post_list = Article.objects.filter(category=self.category)
        context['category'] = self.category
        context['post_list'] = post_list
        return context



class TagView(ListView):
    model = Article
    template_name = 'tag-view.html'
# Get the category id from the url
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return Article.objects.filter(tags=self.tag)
# Add the category in our dicctionary
    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        post_list = Article.objects.filter(tags=self.tag)
        context['tag'] = self.tag
        context['post_list'] = post_list
        return context


class AuthorView(ListView):
    model = Article
    template_name = 'user-view.html'
# Get the category id from the url
    def get_queryset(self):
        self.author = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        return Article.objects.filter(author=self.author)
# Add the category in our dicctionary
    def get_context_data(self, **kwargs):
        context = super(AuthorView, self).get_context_data(**kwargs)
        post_list = Article.objects.filter(author=self.author)
        context['author'] = self.author
        context['post_list'] = post_list
        return context


def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def error_500(request):
        data = {}
        return render(request,'500.html', data)
