from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label='Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Digite seu usuario', 'class': 'form-control'}
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
           attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'} 
        ),
    )
    

class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadsatro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ex: João Silva', 'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={'placeholder': 'Ex: joao@gmail.com', 'class': 'form-control'}
        )
    )
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
           attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'} 
        ),
    )
    senha_2 = forms.CharField(
        label='Confirme sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
           attrs={'placeholder': 'Digite sua senha novamente', 'class': 'form-control'} 
        ),
    )