from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

from .forms import ClienteForm, TecnicoForm, TicketsForm
from django.shortcuts import redirect, get_object_or_404

from .models import Cliente, Tecnico, Ticket

# Create your views here.
@csrf_protect
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redireccionar según el grupo al que pertenece el usuario
            if user.groups.filter(name='Administracion').exists():
                return redirect('adm_dashboard')
            elif user.groups.filter(name='Tecnico').exists():
                return redirect('tec_dashboard')
            elif user.groups.filter(name='Cliente').exists():
                return redirect('cli_dashboard')
        else:
            return HttpResponse("Usuario o Contraseña incorrecta")
    # Devolver la plantilla de inicio de sesión para GET
    return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def index(request):
    return redirect('login')


##SECCION DE ADMINISTRACION
def adm_dashboard(request):
    return render(request, 'administracion/tickets.html')

def adm_tickets(request):
    tickets = Ticket.objects.all()

    return render(request, 'administracion/tickets.html', {'tickets': tickets})

def adm_equipo(request):
    # Obtener todos los técnicos
    equipos = Tecnico.objects.all()

    return render(request, 'administracion/equipo.html', {'equipos': equipos})

def adm_clientes(request):
    # Obtener todos los clientes
    clientes = Cliente.objects.all()
    return render(request, 'administracion/clientes.html', {'clientes': clientes})

def crear_ticket(request):
    if request.method == 'POST':
        form = TicketsForm(request.user.cliente, request.POST)
        if form.is_valid():
            form.save()
            return redirect('adm_tickets')  # Redirige a la página de éxito
    else:
        form = TicketsForm()
    return render(request, 'administracion/crear_tickets.html', {'form': form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adm_clientes')  # Redirige a la página de éxito
    else:
        form = ClienteForm()
    return render(request, 'administracion/crear_cliente.html', {'form': form})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.user.delete()  # Eliminar el usuario asociado al cliente
        cliente.delete()  # Eliminar el cliente
    return redirect('adm_clientes')  # Redirigir a la página deseada después de eliminar el cliente

def eliminar_tecnico(request, tecnico_id):
    tecnico = get_object_or_404(Tecnico, pk=tecnico_id)
    if request.method == 'POST':
        tecnico.user.delete()  # Eliminar el usuario asociado al cliente
        tecnico.delete()  # Eliminar el cliente
    return redirect('adm_equipo')  # Redirigir a la página deseada después de eliminar el cliente

def crear_tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adm_equipo')  # Redirige a la página de éxito
    else:
        form = TecnicoForm()
    return render(request, 'administracion/crear_tecnico.html', {'form': form})

def adm_profile(request):
    administrador = request.user

    print(administrador)

    return render(request, 'administracion/profile.html', {'administrador':administrador})

##SECCION DE CLIENTES
def cli_dashboard(request):
    return render(request, 'cliente/dashboard.html')


##SECCION DE TECNICOS
def tec_dashboard(request):
    return render(request, 'tecnico/dashboard.html')

