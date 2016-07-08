from django.contrib import admin
from appmightyrestaurant.models import Worker, MenuItem, Order, FoodType


class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'workertype', 'hirement']
admin.site.register(Worker, WorkerAdmin)


class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ['category']
admin.site.register(FoodType, FoodTypeAdmin)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'foodtype', 'price']
admin.site.register(MenuItem, MenuItemAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'orderitem', 'foodstatus', 'paidstatus']
admin.site.register(Order)
