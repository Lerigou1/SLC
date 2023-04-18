from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login


# Create your views here.

def index(request):
    return render(request, "login/index.html")

def login_view(request):
    if request.method == "GET":
        return render(request, "login/login.html")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("listas:index"))
        else:
            return render(request, "login/login.html", {
                "message": "Dados Incorretos"
            })

def cadastro(request):
    if request.method == "GET":
        return render (request, 'login/cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return render(request, "login/cadastro.html", {
                "message": "Usuário existente"
            })

        user = User.objects.create_user(username=username, password=senha)
        user.save()

        return HttpResponseRedirect("login:index")

def logout_view(request):
    logout(request)
    return render(request, "login/index.html", {
                "message": ""
            })