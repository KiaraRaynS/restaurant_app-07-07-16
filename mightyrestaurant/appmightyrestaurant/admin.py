from django.contrib import admin
from appmightyrestaurant.models import Worker, MenuItem, Order, FoodType, CustomerTable


class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'workertype', 'hirement']
admin.site.register(Worker, WorkerAdmin)


class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ['category']
admin.site.register(FoodType, FoodTypeAdmin)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'foodtype', 'price']
admin.site.register(MenuItem, MenuItemAdmin)


class CustomerTableAdmin(admin.ModelAdmin):
    list_display = ['partyname']
admin.site.register(CustomerTable, CustomerTableAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['tableid', 'customer', 'orderitem', 'foodstatus', 'paidstatus']
admin.site.register(Order, OrderAdmin)
