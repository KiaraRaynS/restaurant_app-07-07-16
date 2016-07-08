from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from appmightyrestaurant.models import Worker, MenuItem, Order, FoodType, CustomerTable
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
                        'foodtypes': FoodType.objects.all().order_by('ordernumber'),
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


# Owner related Views
class CreateMenuItemView(CreateView):
    model = MenuItem
    template_name = 'createmenuitemview.html'
    fields = ['title', 'description', 'price']

    def form_valid(self, form):
        form.instance.foodtype = FoodType.objects.get(id=self.kwargs['pk'])
        return super(CreateMenuItemView, self).form_valid(form)
    success_url = '/'


class CreateFoodTypeView(CreateView):
    model = FoodType
    template_name = 'createfoodtypeview.html'
    fields = ['category']
    success_url = '/'


class UpdateFoodTypeView(UpdateView):
    model = FoodType
    template_name = 'updatefoodtypeview.html'
    fields = ['category']
    success_url = '/'


class DeleteMenuItemView(DeleteView):

    def get_object(self):
        menuitem = MenuItem.objects.get(id=self.kwargs['pk'])
        return menuitem


# Server Related Views
class SeatCustomersView(CreateView):
    model = CustomerTable
    fields = ['partyname']
    success_url = '/'
