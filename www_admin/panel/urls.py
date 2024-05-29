from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('movies/<int:movie_id>', views.movies, name='movies'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('destacadas/', views.destacadas, name='destacadas'),
    path('cart/', views.cart, name='cart'),
    path('delete_ticket/<int:Id>/', views.delete_ticket, name='delete_ticket'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
