from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from appmightyrestaurant.views import IndexView, RegisterView, ProfileView
from appmightyrestaurant.views import UpdateMenuItemView
# Owner Views
from appmightyrestaurant.views import CreateMenuItemView, DeleteMenuItemView, UpdateFoodTypeView, CreateFoodTypeView
# Server Views
from appmightyrestaurant.views import SeatCustomersView, TakeCustomerOrderView, TableOrdersView, OrderUpdateView
# Cook Views
from appmightyrestaurant.views import ConfirmOrderDoneView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='indexview'),
    # User related URLS
    url(r'^register/$', RegisterView.as_view(), name='registerview'),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profileview'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    # Owner Actions
    url(r'^newmenuitem/(?P<pk>\d+)$', CreateMenuItemView.as_view(), name='createmenuitemview'),
    url(r'^updatemenu/(?P<pk>\d+)/$', UpdateMenuItemView.as_view(), name='updatemenuitemview'),
    url(r'^deletemenuitem/(?P<pk>\d+)/$', DeleteMenuItemView.as_view(), name='deletemenuitemview'),
    url(r'^newcategory/$', CreateFoodTypeView.as_view(), name='createfoodtypeview'),
    url(r'^updatefoodtype/(?P<pk>\d+)/$', UpdateFoodTypeView.as_view(), name='updatefoodtypeview'),
    # Server Actions
    url(r'^customertable/$', SeatCustomersView.as_view(), name='seatcustomersview'),
    url(r'^customertable/(?P<pk>\d+)/takeorder/$', TakeCustomerOrderView.as_view(), name='takecustomerorderview'),
    url(r'^customertable/(?P<pk>\d+)/$', TableOrdersView.as_view(), name='tableordersview'),
    url(r'^order/serverrevise/(?P<pk>\d+)/$', OrderUpdateView.as_view(), name='orderupdateview'),
    # Cook options
    url(r'^order/confirmcooked/(?P<pk>\d+)/$', ConfirmOrderDoneView.as_view(), name='confirmorderdoneview'),
]
