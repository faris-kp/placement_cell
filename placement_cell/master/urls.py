from django.urls import path
from master.views import AdminHome


urlpatterns = [

 path('adminpanel',AdminHome.as_view(),name='A_home'),

]
