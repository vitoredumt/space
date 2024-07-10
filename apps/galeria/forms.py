from django import forms

from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        fields = '__all__'
        exclude = ['publicada',]
        labels = {
            'nome': 'Nome',
            'legenda': 'Legenda',
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'foto': 'Foto',
            'data': 'Data',
            'usuario': 'Usuário',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }