from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        messages.add_message(request, constants.SUCCESS, "Cadastro Realizado com Sucesso!")
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, "'Senha' e 'Confirmar Senha' deve ser iguais")
            return redirect("/usuarios/cadastro/")

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A Senha deve ter 6 ou mais caracteres')
            return redirect("/usuarios/cadastro/")

        users = User.objects.filter(username = username)
        if users.exists():
            messages.add_message(request, constants.ERROR, "Já existe um usuário com este 'username'")
            return redirect("/usuarios/cadastro/")


        User.objects.create_user(
            username = username,
            password = senha
        )
        return redirect("/usuarios/cadastro/")

#
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')