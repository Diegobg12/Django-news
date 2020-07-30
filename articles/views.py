from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
UserPassesTestMixin)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'  

class ArticleDetailLView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryView(ListView):
    model = Article
    template_name = 'article_category.html'

# Get the category id from the url
    def get_queryset(self):
        self.category = get_object_or_404(category, pk=self.kwargs['pk'])
        return Article.object.filter(category=self.category)
# Add the category in our dicctionary
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context
