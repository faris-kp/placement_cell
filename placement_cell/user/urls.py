from django.urls import path
from user.views import Register,Signin
# from user import views as user_views



urlpatterns = [

        path('signup/',Register,name='Register'),
        path('signin/',Signin.as_view(),name='sign_in'),

]
