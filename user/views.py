from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        messages.success(request,("wrong username or password !!! please try again"))
        return redirect('login_user')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("you are logged out !!!"))
    return redirect('index')