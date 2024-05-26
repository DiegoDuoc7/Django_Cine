from panel.models import Pelicula

peliculas = [
    {
        "id": 1,
        "year": 2024,
        "genre": "Animacion",
        "title": "Kung Fu Panda 4",
        "actors": "Jack Black, Angelina Jolie, Dustin Hoffman",
        "director": "Jennifer Yuh Nelson",
        "duration": 95,
        "imageUrl": "imagenes/WhatsApp Image 2024-04-05 at 20.27.48.jpeg",
        "synopsis": "Po se enfrenta a una nueva amenaza y debe buscar dentro de si para encontrar la fuerza necesaria para superarla.",
        "trailerUrl": "imagenes/Kung Fu Panda 4 _ Trailer Oficial (Universal Pictures) - HD.mp4",
        "description": "Esta es una breve descripcion de Kung Fu Panda 4"
    },
    {
        "id": 2,
        "year": 2021,
        "genre": "Ciencia Ficcion",
        "title": "Dune",
        "actors": "Timothee Chalamet, Zendaya, Oscar Isaac",
        "director": "Denis Villeneuve",
        "duration": 155,
        "imageUrl": "imagenes/WhatsApp Image 2024-04-05 at 20.27.44.jpeg",
        "synopsis": "Paul Atreides debe viajar al planeta mas peligroso del universo para asegurar el futuro de su familia y su pueblo.",
        "trailerUrl": "imagenes/Duna - Trailer Oficial.mp4",
        "description": "Esta es una breve descripcion de Dune"
    },
    {
        "id": 3,
        "year": 2023,
        "genre": "Terror",
        "title": "BagHead",
        "actors": "Freya Allan, Ruby Barker, Peter Lanzani",
        "director": "Alberto Corredor Marina",
        "duration": 89,
        "imageUrl": "imagenes/WhatsApp Image 2024-04-05 at 20.27.40.jpeg",
        "synopsis": "Una entidad misteriosa con una bolsa en la cabeza aterroriza a aquellos que se atreven a enfrentarlo.",
        "trailerUrl": "imagenes/BAGHEAD _ Official Trailer _ STUDIOCANAL.mp4",
        "description": "Esta es una breve descripcion de BagHead"
    }
]

for pelicula in peliculas:
    print(f"Insertando película: {pelicula['title']}")
    print(f"ID: {pelicula['id']}")
    print(f"Año: {pelicula['year']}")
    print(f"Género: {pelicula['genre']}")
    print(f"Actores: {pelicula['actors']}")
    print(f"Director: {pelicula['director']}")
    print(f"Duración: {pelicula['duration']}")
    print(f"URL de la imagen: {pelicula['imageUrl']}")
    print(f"Sinopsis: {pelicula['synopsis']}")
    print(f"URL del tráiler: {pelicula['trailerUrl']}")
    print(f"Descripción: {pelicula['description']}")
    Pelicula.objects.create(**pelicula)
    print(f"Película {pelicula['title']} insertada correctamente.\n")
