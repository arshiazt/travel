from django.shortcuts import render,redirect
from django.contrib.auth  import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.

def signup_view(request):

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
        
    form = UserCreationForm()
    context = {'form':form}
    return render(request,'accounts/signup.html',context)

def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
        
    form = LoginForm()
    context = {'form':form}
    return render(request,'accounts/login.html',context)
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')