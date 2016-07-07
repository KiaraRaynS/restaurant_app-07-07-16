from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from appmightyrestaurant.models import Worker, MenuItem, Order
from django.core.urlresolvers import reverse_lazy


class IndexView(TemplateView):
    template_name = 'indexview.html'


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'


class ProfileView(UpdateView):
    model = Worker
    fields = ['name', 'workertype']
    template_name = 'profileview.html'
    success_url = reverse_lazy('profileview')

    def get_object(self, queryset=None):
        return self.request.user
