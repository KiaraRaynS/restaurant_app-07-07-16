from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from appmightyrestaurant.views import IndexView, RegisterView, ProfileView
from appmightyrestaurant.views import UpdateMenuItemView
# Owner related Views
from appmightyrestaurant.views import CreateMenuItemView, CreateFoodTypeView, UpdateFoodTypeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='indexview'),
    # User related URLS
    url(r'^register/$', RegisterView.as_view(), name='registerview'),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profileview'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    # Owner actions
    url(r'^newmenuitem/(?P<pk>\d+)$', CreateMenuItemView.as_view(), name='createmenuitemview'),
    url(r'^updatemenu/(?P<pk>\d+)/$', UpdateMenuItemView.as_view(), name='updatemenuitemview'),
    url(r'^newcategory/$', CreateFoodTypeView.as_view(), name='createfoodtypeview'),
    url(r'^updatefoodtype/(?P<pk>\d+)/$', UpdateFoodTypeView.as_view(), name='updatefoodtypeview'),
]
