from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import (LoginRequiredMixin,
UserPassesTestMixin)
from django.urls import reverse_lazy
from .forms import *
from django.views.generic.edit import DeleteView, UpdateView, CreateView


# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class EditUser(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    model = CustomUser
    template_name = 'edituser.html'

    def get(self, request, **kwargs):
        self.object = CustomUser.objects.get(username=self.request.user)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)


    def get_object(self, queryset=None):
        return self.request.user