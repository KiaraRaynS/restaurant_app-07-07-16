from django.shortcuts import render
from django.db.models import Sum
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
                        'orders': Order.objects.order_by('orderdate'),
                        }
                return context
            # If the user is a server
            if worker.workertype == 'server':
                context = {
                        'worker': worker,
                        'tables': CustomerTable.objects.all(),
                        'orders': Order.objects.filter(server=worker).filter(paidstatus=False).order_by('orderdate'),
                        }
                return context

        def post(self, request, *args, **kwargs):
            return updateview.as_view()(request)


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
    success_url = '/'

    def get_object(self):
        menuitem = MenuItem.objects.get(id=self.kwargs['pk'])
        return menuitem


# Server Related Views
class SeatCustomersView(CreateView):
    model = CustomerTable
    fields = ['partyname']
    success_url = '/'


class TakeCustomerOrderView(CreateView):
    model = Order
    fields = ['orderitem', 'notes']
    success_url = '/'

    def form_valid(self, form):
        form.instance.tableid = CustomerTable.objects.get(id=self.kwargs['pk'])
        form.instance.server = Worker.objects.get(user=self.request.user)
        return super(TakeCustomerOrderView, self).form_valid(form)


class TableOrdersView(TemplateView):
    template_name = 'tableordersview.html'

    def get_context_data(self, **kwargs):
        tableid = self.kwargs['pk']
        customertable = CustomerTable.objects.get(id=tableid)
        context = {
                'table': customertable,
                'orders': Order.objects.filter(tableid=customertable),
                'total': Order.objects.filter(tableid=customertable).aggregate(Sum('orderitem__price')),
                }
        return context


class OrderUpdateView(UpdateView):
    template_name = 'orderupdateneeded.html'
    model = Order
    fields = ['revision']
    success_url = '/'

    def get_object(self):
        ordernumber = self.kwargs['pk']
        return Order.objects.get(id=ordernumber)

    def form_valid(self, form):
        form.instance.revisionstatus = True
        return super(OrderUpdateView, self).form_valid(form)


# Cook Related Views
class ConfirmOrderDoneView(UpdateView):
    model = Order
    fields = ['foodstatus']
    success_url = '/'
    template_name = 'confirmorderdoneview.html'

    def get_object(self):
        ordernumber = self.kwargs['pk']
        return Order.objects.get(id=ordernumber)

    def form_valid(self, form):
        form.instance.foodstatus = True
        return super(ConfirmOrderDoneView, self).form_valid(form)
