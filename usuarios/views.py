from django.shortcuts import render, redirect

from usuarios.forms import LoginForm, CadastroForm

from django.contrib.auth.models import User

from django.contrib import auth

# Create your views here.
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome, 
                password=senha
            )
            if usuario != None:
                auth.login(request, usuario)
                return redirect('index')
            else:
                return redirect('login')

         

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect ('cadastro')

            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    return render(request, 'usuarios/logout.html')