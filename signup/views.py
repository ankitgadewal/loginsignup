from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        newuser = User.objects.create_user(username=username, password=password)
        newuser.save()
    else:
        return HttpResponse("you are Unauthorized")
    return render(request, 'signup.html', {'username':username})

def userlogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user:
            login(request, user)
            messages.success(request, "you are successfullt logged in")
            return render(request, 'loginpage.html', {'user': user})
        else:
            return HttpResponse("username or password incorrect")

def userlogout(request):
    logout(request)
    return render(request, 'userlogout.html')
