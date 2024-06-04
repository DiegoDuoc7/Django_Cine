from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from panel.models import Pelicula, Ticket
from panel.forms.contacto_form import ContactForm
from panel.forms.ticket_form import TicketForm
from panel.forms.login_form import LoginForm
from panel.forms.register_form import RegisterForm  # Importando el formulario de registro
from django.contrib.auth.decorators import login_required

import os

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def movies(request, movie_id):
    try:
        pelicula = Pelicula.objects.get(id=movie_id)
    except Pelicula.DoesNotExist:
        return HttpResponse("Película no encontrada", status=404)
    url = "static/" + pelicula.imageUrl
    url = url[7:]  # Quitando los primeros 7 caracteres
    print(url)
    if request.method == 'POST':
        form = TicketForm(request.POST, initial={'movieName': pelicula.title})
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha agregado la orden correctamente al carrito')

    else:
        form = TicketForm(initial={'movieName': pelicula.title})
    return render(request, 'movies.html', {'movie': pelicula, 'imagen_url': url, 'form': form})

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu solicitud de contacto ha sido enviada exitosamente.')
            # Aquí puedes agregar lógica adicional, como enviar un correo electrónico
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

@login_required
def destacadas(request):
    return render(request, 'destacadas.html')

@login_required
def cart(request):
    if request.method == 'POST':
        messages.success(request, '¡Pongámosle un 7, Profe!')
        return redirect('cart')
    tickets = Ticket.objects.all()
    total = sum((3000 * ticket.quantity if ticket.type == 'child' else 7000 * ticket.quantity) for ticket in tickets)
    return render(request, 'cart.html', {'tickets': tickets, 'total': total})

@login_required
def delete_ticket(request, Id):
    print("Entrando a la función delete_ticket")
    print("ID del ticket recibido:", Id)
    try:
        ticket = get_object_or_404(Ticket, Id=Id)
        print("Ticket encontrado:", ticket)
    except Exception as e:
        print("Error al obtener el ticket:", e)
        raise Http404("Ticket no encontrado")
    
    try:
        ticket.delete()
        print("Ticket eliminado correctamente")
    except Exception as e:
        print("Error al eliminar el ticket:", e)
        raise Http404("Error al eliminar el ticket")
    
    return redirect('cart')

def login(request):
    print("Entrando a la función login")
    if request.method == 'POST':
        print("Método POST detectado")
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            print("Formulario de login es válido")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"Datos recibidos - Username: {username}, Password: {password}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Autenticación exitosa")
                auth_login(request, user)
                return redirect('index')
            else:
                print("Autenticación fallida: Usuario o contraseña incorrectos")
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            print("Formulario de login no es válido")
            messages.error(request, 'Usuario o contraseña incorrectos.')

    else:
        print("Método GET detectado")
        form = LoginForm()
    print("Renderizando la plantilla login.html")
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')