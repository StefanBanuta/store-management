from django import forms
from .models import Client,ProdusAlimentar,Producator,Achizitie,Comanda
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nume utilizator')
    password = forms.CharField(label='Parola', widget=forms.PasswordInput)

class AdaugaClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nume', 'prenume', 'adresa']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class AdaugaProdusAlimentarForm(forms.ModelForm):
    class Meta:
        model = ProdusAlimentar
        fields = ['denumire', 'data_producere', 'data_expirare']


class AdaugaProducatorForm(forms.ModelForm):
    class Meta:
        model = Producator
        fields = ['denumire', 'tara_origine','adresa']

class AchizitieForm(forms.ModelForm):
    class Meta:
        model = Achizitie
        fields = ['client', 'produs', 'data_achizitie']

class AdaugaComandaForm(forms.ModelForm):
    class Meta:
        model = Comanda
        fields = ['produs', 'producator', 'data_comanda']