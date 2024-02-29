import random
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

from django import forms
from .models import Cliente, Tecnico
from django.contrib.auth.models import User, Group

def generar_username(nombre, apellido):
    # Obtener las dos primeras letras del nombre y del apellido
    letras_nombre = nombre[:2].lower()
    letras_apellido = apellido[:2].lower()
    # Generar un número aleatorio entre 0 y 9999
    numero_aleatorio = random.randint(0, 9999)
    # Combinar las letras y el número para formar el username
    username = f"{letras_nombre}{letras_apellido}{numero_aleatorio}"
    return username

def generar_contraseña():
    # Generar una contraseña aleatoria de longitud 8
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    contraseña = ''.join(random.choice(caracteres) for i in range(8))
    return contraseña

def crear_cliente(nombre, apellido, comuna):
    # Generar username y contraseña aleatorios
    username = generar_username(nombre, apellido)
    contraseña = generar_contraseña()
    # Crear el usuario
    user = User.objects.create_user(username=username, password=contraseña)
    # Asignar el grupo 'cliente' al usuario
    grupo_cliente, creado = Group.objects.get_or_create(name='Cliente')
    user.groups.add(grupo_cliente)
    # Crear el cliente asociado al usuario
    cliente = Cliente.objects.create(user=user, comuna=comuna)
    return cliente

def crear_tecnico(nombre, apellido, nivel):
    # Generar username y contraseña aleatorios
    username = generar_username(nombre, apellido)
    contraseña = generar_contraseña()
    # Crear el usuario
    user = User.objects.create_user(username=username, password=contraseña)
    # Asignar el grupo 'tecnico' al usuario
    grupo_tecnico, creado = Group.objects.get_or_create(name='Tecnico')
    user.groups.add(grupo_tecnico)
    # Crear el tecnico asociado al usuario
    tecnico = Tecnico.objects.create(user=user, nivel=nivel)
    return tecnico

class ClienteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    comuna = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')
        comuna = cleaned_data.get('comuna')
        # Generar username y contraseña aleatorios
        username = generar_username(nombre, apellido)
        contraseña = generar_contraseña()
        # Asignar el grupo 'cliente' al usuario
        grupo_cliente, creado = Group.objects.get_or_create(name='Cliente')
        cleaned_data['grupo'] = grupo_cliente
        cleaned_data['username'] = username
        cleaned_data['password'] = make_password(contraseña)
        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['nombre'],
            last_name=self.cleaned_data['apellido']
        )
        user.groups.add(self.cleaned_data['grupo'])
        cliente = Cliente.objects.create(
            user=user,
            comuna=self.cleaned_data['comuna']
        )
        return cliente

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'comuna']

class TecnicoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    nivel = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')
        nivel = cleaned_data.get('nivel')
        # Generar username y contraseña aleatorios
        username = generar_username(nombre, apellido)
        contraseña = generar_contraseña()
        # Asignar el grupo 'tecnico' al usuario
        grupo_tecnico, creado = Group.objects.get_or_create(name='Tecnico')
        cleaned_data['grupo'] = grupo_tecnico
        cleaned_data['username'] = username
        cleaned_data['password'] = make_password(contraseña)
        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['nombre'],
            last_name=self.cleaned_data['apellido']
        )
        user.groups.add(self.cleaned_data['grupo'])
        tecnico = Tecnico.objects.create(
            user=user,
            nivel=self.cleaned_data['nivel']
        )
        return tecnico

    class Meta:
        model = Tecnico
        fields = ['nombre', 'apellido', 'nivel']