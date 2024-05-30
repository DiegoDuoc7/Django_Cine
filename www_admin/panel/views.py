from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse
from django.contrib import messages
from panel.models import Pelicula, Ticket
from panel.forms.contacto_form import ContactForm
from panel.forms.ticket_form import TicketForm

import os

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, 'index.html')


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
            messages.success(request, 'Se ha comprado la orden correctamente al carrito')

    else:
        form = TicketForm(initial={'movieName': pelicula.title})
    return render(request, 'movies.html', {'movie': pelicula, 'imagen_url': url, 'form': form})
def about(request):
    return render(request, 'about.html')

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

def destacadas(request):
    return render(request, 'destacadas.html')
def cart(request):
    tickets = Ticket.objects.all()
    total = sum((3000 * ticket.quantity if ticket.type == 'child' else 7000 * ticket.quantity) for ticket in tickets)
    return render(request, 'cart.html', {'tickets': tickets, 'total': total})
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