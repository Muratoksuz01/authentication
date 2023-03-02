from django.shortcuts import redirect, render,HttpResponse
from django .contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,"index.html")

def signup(request):    
    if request.method=="POST":
# username = request. POST.get('username')
        username = request. POST['username']
        fname = request. POST['fname']
        name = request. POST['lname']
        email = request. POST['email']
        pass1= request. POST['pass1']
        pass2= request. POST['pass2']

        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = name
        myuser.save()
        messages.success(request,"kayıt oldunuz")
        return redirect("signin")
    return render(request,"signup.html")


def signin(request):
    if request.method=="POST":
        username = request. POST['username']
        pass1= request. POST['pass1']
        myuser=authenticate(username=username,password=pass1)

        if myuser is not None:
            login(request,myuser)
            return redirect("home")
        else:
            messages.error(request,"bad Credentials")
            return render(request,"signin.html")
    return render(request,"signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Loged Out Successfully!")
    return redirect("home")