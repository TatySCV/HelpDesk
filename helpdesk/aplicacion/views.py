from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admi_dashboard')
        else:
            return HttpResponse("Usuario o Contraseña incorrecta")

    return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def admi_profile(request):
    return render(request, 'administracion/profile.html')

def admi_dashboard(request):
    return render(request, 'administracion/dashboard.html')