from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('movies/<int:movie_id>', views.movies, name='movies'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('destacadas', views.destacadas, name='destacadas'),
    path('cart/', views.cart, name='cart'),
    path('delete_ticket/<int:Id>', views.delete_ticket, name='delete_ticket'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
