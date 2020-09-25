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


# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html' 


class ArticleDetailLView(FormMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    form_class = CommentForm
 

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    login_url = 'login'
    form_class = ArticleForm

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
        comment.save()
        super().form_valid(form)
        
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
        
# @login_required
# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author
#             comment.comment = post
#             comment.save()
#             return redirect('article_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'add_comment_to_post.html', {'form': form})