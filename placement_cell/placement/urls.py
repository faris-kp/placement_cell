from django.urls import path
from placement.views import Index


urlpatterns = [

 path('',Index.as_view(),name='P_home'),

]
