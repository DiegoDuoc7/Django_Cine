from django import forms
from panel.models import Contacto

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'minlength': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'pattern': '^[^@]+@[^@]*mail[^@]*$'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'minlength': 10}),
        }
        error_messages = {
            'name': {
                'required': 'Este campo es obligatorio.',
                'minlength': 'Este campo debe tener al menos 3 caracteres.',
            },
            'email': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'El correo electrónico no es válido.',
                'pattern': 'El correo electrónico debe contener "mail" después del "@".',
            },
            'message': {
                'required': 'Este campo es obligatorio.',
                'minlength': 'Este campo debe tener al menos 10 caracteres.',
            },
        }

