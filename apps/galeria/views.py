from django.shortcuts import render, get_object_or_404, redirect

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

from django.contrib import messages



def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página')
        return redirect('login')
        
    fotografia = Fotografia.objects.order_by('-data').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografia})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página')
        return redirect('login')

    fotografia = Fotografia.objects.order_by('-data').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografia = fotografia.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {'cards': fotografia})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página')
        return redirect('login')
    
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem cadastrada com sucesso')
            return redirect('index')
        
    return render(request, 'galeria/nova_imagem.html', {'form': form})
        
def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass