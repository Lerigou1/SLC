from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login:login"))
    return render(request, "login/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("login:user"))
        else:
            return render(request, "login/index.html", {
                "message": "Dados Incorretos"
            })
    return render(request, "login/user.html")

def logout_view(request):
    logout(request)
    return render(request, "login/index.html", {
                "message": ""
            })