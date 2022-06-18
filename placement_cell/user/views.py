from django.shortcuts import render,redirect
from requests import request
from user.forms import UserRegisterForm,LoginForm
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User




def Register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        print("")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created for {username} You Are Able To Login')
            return redirect('P_home')
    else:
        form = UserRegisterForm()

    return render(request ,'user/signup.html',{'form':form})


class Signin(View):

    template_name = 'user/signin.html'

    def get(self,request):
        form = LoginForm
        context = {
            'form':form
        }
        return render(request,self.template_name,context)
    
    def post(self,request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username ,password=password)

        if user is not None:
            login(request,user)

            # my_admin = User.objects.get(username=request.user) # for admin check

            # my_res = Restaurant.objects.filter(resn=request.user) $ for organaisation check
            print(request.user)
            my_cus = User.objects.get(user=request.user)
            print(my_cus)
        
            if request.user.is_superuser:
                return redirect('A_home')
            elif my_cus:
                return redirect('P_home')
            else:
                 messages.success(request, f'invalid user')
                 return redirect('sign_in')
        else:
             messages.success(request, f'invalid user')
             return redirect('sign_in')