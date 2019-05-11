from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/users/login')
def dashboard(request):
    print("dashboard:",request)
    return render(request,'dashboard.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/users/dashboard/',user=user.username)
        else:
            messages.warning(request, 'Wrong Username or Password.')
            return render(request, 'login.html')
    return render(request, 'login.html')

def signout(request):
    print('in signout view')
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect(signin)
def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        check_email = User.objects.filter(email__contains=email)
        check_username = User.objects.filter(username__contains=username)
        if not username or not email or not password:
            messages.info(request, 'Please enter all the details.')
            return render(request, 'register.html')
        if check_email:
            messages.info(request, 'The given email is already in use.')
            return render(request, 'register.html')
        if check_username:
            messages.info(request, 'The given username is already in use.')
            return render(request, 'register.html')
        if len(password) < 7 :
            messages.info(request, 'Password should be atleast 6 characters long.')
            return render(request, 'register.html')
        if password != password2:
            messages.warning(request, 'Passwords do not match.')
            return render(request, 'register.html')
        
        username.replace(" ","")
        user = User.objects.create_user(username,email,password)
        user.save()
        messages.success(request,'You are now registered and can log in');
        return redirect(signin)

    return render(request, 'register.html')
    