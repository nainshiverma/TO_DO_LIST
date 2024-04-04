from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        fname=request.POST.get("f_name")
        lname=request.POST.get("l_name")
        password=request.POST.get("password")

        new_user = User.objects.creat(
            username = username,
            first_name = fname,
            last_name = lname
        )

        new_user.set_password(password)
        new_user.save()



    return render(request , "signup.html")


# Create your views here.


def login(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("password")
        user=auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request , user)
            return redirect("dashboard")
        else:
            return redirect("invalid")
    return render(request , "login.html")

