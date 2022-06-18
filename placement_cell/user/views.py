from django.shortcuts import render,redirect
from user.forms import UserRegisterForm
from django.contrib import messages




def Register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created for {username} You Are Able To Login')
            return redirect('P_home')
    else:
        form = UserRegisterForm()

    return render(request ,'users/Register.html',{'form':form})