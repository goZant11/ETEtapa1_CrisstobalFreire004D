from django import forms
from django.forms import ModelForm, fields
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import DatosColaboradores




class ColabForm(forms.ModelForm):
    class Meta:
        model= DatosColaboradores
        fields = ['rut', 'nombre', 'telefono', 'dir', 'email', 'pais', 'clave', 'imagen']
        labels ={
            'rut': 'Rut del Colaborador',
            'nombre': 'Nombre del Colaborador',
            'telefono': 'Telefono del Colaborador',
            'dir': 'Dirección del Colaborador',
            'email': 'Correo del Colaborador',
            'pais': 'Pais del Colaborador',
            'clave': 'Contraseña del Colaborador',
            'imagen': 'Foto del Colaborador',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese RUT',
                    'id': 'rut'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre',
                    'id': 'nombre'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Telefono',
                    'id': 'telefono'
                }
            ),
            'dir': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Dirección',
                    'id': 'dir'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Correo',
                    'id': 'email'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Pais',
                    'id': 'pais'
                }
            ),
            'clave': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Clave',
                    'id': 'rut'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un archivo',
                    'id': 'imagen'
                }
            ),
        }
