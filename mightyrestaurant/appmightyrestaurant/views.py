from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from appmightyrestaurant.models import Worker, MenuItem, Order
from django.core.urlresolvers import reverse_lazy


class IndexView(TemplateView):
    template_name = 'indexview.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        print(user)
        if user.is_authenticated():
            worker = Worker.objects.get(user=user)
            print(worker.workertype)
            # If the user is an owner
            if worker.workertype == 'owner':
                context = {
                        'worker': worker,
                        'items': MenuItem.objects.all(),
                        }
                return context
            # If the user is a cook
            if worker.workertype == 'cook':
                context = {
                        'worker': worker,
                        'orders': Order.objects.filter(foodstatus=False),
                        }
                return context
            # If the user is a server
            if worker.workertype == 'server':
                context = {
                        'worker': worker,
                        'orders': Order.objects.filter(server=worker).filter(paidstatus=False),
                        }
                return context


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'


class ProfileView(UpdateView):
    model = Worker
    fields = ['name', 'workertype']
    template_name = 'profileview.html'
    success_url = '/'

    def get_object(self, queryset=None):
        print(self.request.user)
        user = self.request.user
        instance = Worker.objects.get(user=user)
        return instance


class UpdateMenuItemView(UpdateView):
    model = MenuItem
    fields = ['title', 'foodtype', 'description', 'price']
    success_url = '/'

    def get_object(self, queryset=None):
        menuitemid = self.kwargs['pk']
        menuitem = MenuItem.objects.get(id=menuitemid)
        return menuitem
