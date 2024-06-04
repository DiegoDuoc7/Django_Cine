from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, EmailValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name='correo electrónico', max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name='fecha de registro', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='último acceso', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

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
    type = models.CharField(max_length=10, choices=[('child', 'Niño'), ('adult', 'Adulto')])
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.movieName} - {self.type} - {self.quantity} boletos"
