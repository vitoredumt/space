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

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome: 
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O usuário não pode conter espaços')
            else:
                return nome

    def clean_senha_2(self):

        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas devem ser iguais')
            else:
                return senha_2