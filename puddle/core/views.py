from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Client,ProdusAlimentar,Producator,Achizitie,Comanda
from .forms import AdaugaClientForm,ClientForm,UserCreationForm,LoginForm,AdaugaProdusAlimentarForm,AdaugaProducatorForm,AchizitieForm,AdaugaComandaForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test


def pagina_principala(request):
    return render(request, 'core/pagina_principala.html', {'titlu_pagina': 'Acasă'})

def tabela_clienti(request):
    clienti = Client.objects.all()
    form = AdaugaClientForm()

    if request.method == 'POST':
        form = AdaugaClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabela_clienti')

    return render(request, 'core/tabela_clienti.html', {'clienti': clienti, 'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def sterge_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('tabela_clienti') 

@login_required
def modifica_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('tabela_clienti')
    else:
        form = ClientForm(instance=client)
    return render(request, 'core/modifica_client.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect('/login/')  
    else:
        form = UserCreationForm()
    
    return render(request, 'core/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})



def tabela_produse_alimentare(request):
    produse = ProdusAlimentar.objects.all()
    form = AdaugaProdusAlimentarForm()

    if request.method == 'POST':
        form = AdaugaProdusAlimentarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produse_alimentare')

    return render(request, 'core/lista_produse_alimentare.html', {'produse': produse, 'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def sterge_produs_alimentar(request, pk):
    produs = get_object_or_404(ProdusAlimentar, pk=pk)
    produs.delete()
    return redirect('lista_produse_alimentare') 

@login_required
def modifica_produs_alimentar(request, produs_id):
    produs = get_object_or_404(ProdusAlimentar, pk=produs_id)
    if request.method == 'POST':
        form =AdaugaProdusAlimentarForm(request.POST, instance=produs)
        if form.is_valid():
            form.save()
            return redirect('lista_produse_alimentare')
    else:
        form = AdaugaProdusAlimentarForm(instance=produs)
    return render(request, 'core/modifica_produs_alimentar.html', {'form': form})



def tabela_producatori(request):
    producatori = Producator.objects.all()
    form = AdaugaProducatorForm()

    if request.method == 'POST':
        form = AdaugaProducatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabela_producatori')

    return render(request, 'core/tabela_producatori.html', {'producatori': producatori, 'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def sterge_producator(request, pk):
    producator = get_object_or_404(Producator, pk=pk)
    producator.delete()
    return redirect('tabela_producatori') 

@login_required
def modifica_producator(request, producator_id):
    producator = get_object_or_404(Producator, pk=producator_id)
    if request.method == 'POST':
        form = AdaugaProducatorForm(request.POST, instance=producator)
        if form.is_valid():
            form.save()
            return redirect('tabela_producatori')
    else:
        form = AdaugaProducatorForm(instance=producator)
    return render(request, 'core/modifica_producator.html', {'form': form})



def tabela_achizitii(request):
    achizitii = Achizitie.objects.all()
    form = AchizitieForm()  

    if request.method == 'POST':
        form = AchizitieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabela_achizitii')

    return render(request, 'core/tabela_achizitii.html', {'achizitii': achizitii, 'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def sterge_achizitie(request, pk):
    achizitie = get_object_or_404(Achizitie, pk=pk)
    achizitie.delete()
    return redirect('tabela_achizitii') 

@login_required
def modifica_achizitie(request, achizitie_id):
    achizitie = get_object_or_404(Achizitie, pk=achizitie_id)
    if request.method == 'POST':
        form = AchizitieForm(request.POST, instance=achizitie)
        if form.is_valid():
            form.save()
            return redirect('tabela_achizitii')
    else:
        form = AchizitieForm(instance=achizitie)
    return render(request, 'core/modifica_achizitie.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def sterge_comanda(request, pk):
    comanda = get_object_or_404(Comanda, pk=pk)
    comanda.delete()
    return redirect('tabela_comenzi') 

@login_required
def modifica_comanda(request, comanda_id):
    comanda = get_object_or_404(Comanda, pk=comanda_id)
    if request.method == 'POST':
        form = AdaugaComandaForm(request.POST, instance=comanda)
        if form.is_valid():
            form.save()
            return redirect('tabela_comenzi')
    else:
        form = AdaugaComandaForm(instance=comanda)
    return render(request, 'core/modifica_comanda.html', {'form': form})

def tabela_comenzi(request):
    comenzi = Comanda.objects.all()
    form = AdaugaComandaForm()

    if request.method == 'POST':
        form = AdaugaComandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabela_comenzi')

    return render(request, 'core/tabela_comenzi.html', {'comenzi': comenzi, 'form': form})




def test(request):
    return HttpResponse("Funcția de test funcționează corect!")


