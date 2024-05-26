from panel.models import Pelicula

# Agregar mensajes de depuración
print("Iniciando la eliminación de todas las películas...")
peliculas_eliminadas, _ = Pelicula.objects.all().delete()
print(f"Se han eliminado {peliculas_eliminadas} películas.")
print("Eliminación completada.")
