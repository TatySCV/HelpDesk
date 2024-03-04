"""
URL configuration for helpdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),

    path('accounts/login', views.login_user, name='login'),
    path('accounts/logout', views.logout_user, name='logout'),

    path('adm/dashboard', views.adm_dashboard, name='adm_dashboard'),
    path('adm/tickets', views.adm_tickets, name='adm_tickets'),
    path('adm/equipo', views.adm_equipo, name='adm_equipo'),
    path('adm/clientes', views.adm_clientes, name='adm_clientes'),
    path('adm/profile', views.adm_profile, name='adm_profile'),
    path('adm/create/cli', views.crear_cliente, name='create_cli'),
    path('adm/create/tec', views.crear_tecnico, name='create_tec'),
    path('adm/create/tick', views.crear_ticket, name='create_tick'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('eliminar_tecnico/<int:tecnico_id>/', views.eliminar_tecnico, name='eliminar_tecnico'),

    path('cli/dashboard', views.cli_dashboard, name='cli_dashboard'),
    path('tec/dashboard', views.tec_dashboard, name='tec_dashboard'),


]
