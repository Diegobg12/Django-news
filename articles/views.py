from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
UserPassesTestMixin)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *
from django.views.generic.edit import FormMixin

class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = "/contact/"
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html' 


class ArticleDetailLView(FormMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    form_class = CommentForm
 

class ArticleUpdateView(AdminStaffRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    login_url = 'login'
    form_class = ArticleForm

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(AdminStaffRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(AdminStaffRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    login_url = 'login'
    form_class = ArticleForm


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Comment
    fields = ['comment']

    def form_valid(self, form):
        comment=form.save(commit=False)
        comment.article=get_object_or_404(Article, pk=self.kwargs['pk'])
        comment.author = self.request.user
        comment=form.save(commit=False)
        comment.save()
        return super().form_valid(form)
        
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    def get_success_url(self):
        articleid = self.kwargs['pk']
        return reverse_lazy('article_detail', kwargs={'pk': articleid})