from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, EmailValidator


class Pelicula(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    actors = models.CharField(max_length=255)
    director = models.CharField(max_length=100)
    duration = models.IntegerField()
    imageUrl = models.CharField(max_length=255)
    synopsis = models.TextField()
    trailerUrl = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contacto(models.Model):
    name = models.CharField(max_length=100, validators=[
        MinLengthValidator(3),
        RegexValidator(regex='^[a-zA-Z ]+$', message='El nombre solo puede contener letras y espacios.')
    ])
    email = models.EmailField(validators=[
        EmailValidator(),
        RegexValidator(regex='^[^@]+@[^@]*mail', message='El correo debe ser válido y contener "mail".')
    ])
    message = models.TextField(validators=[
        MinLengthValidator(10)
    ])

    def __str__(self):
        return self.name

class Ticket(models.Model):
    Id = models.IntegerField(primary_key=True)
    movieName = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=[('child', 'Child'), ('adult', 'Adult')])
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.movieName} - {self.type} - {self.quantity}"
