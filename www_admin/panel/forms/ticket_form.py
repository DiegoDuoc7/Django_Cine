from django import forms
from panel.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['movieName', 'type', 'quantity']
        widgets = {
            'movieName': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
        labels = {
            'movieName': 'Nombre de la Película',
            'type': 'Tipo',
            'quantity': 'Cantidad',
        }
        error_messages = {
            'movieName': {
                'required': 'Este campo es obligatorio.',
            },
            'type': {
                'required': 'Este campo es obligatorio.',
            },
            'quantity': {
                'required': 'Este campo es obligatorio.',
                'min': 'La cantidad debe ser al menos 1.',
            },
        }
