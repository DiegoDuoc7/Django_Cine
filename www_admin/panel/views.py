from django.shortcuts import render
from django.http import HttpResponse
from panel.models import Pelicula
from panel.forms.contacto_form import ContactForm

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
    return render(request, 'movies.html', {'movie': pelicula, 'imagen_url': url})
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes agregar lógica adicional, como enviar un correo electrónico
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def destacadas(request):
    return render(request, 'destacadas.html')


