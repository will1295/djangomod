from django import forms

class ProvForm(forms.Form):
    nombre=forms.CharField(max_length=100)
    telefono=forms.CharField(max_length=8)
    persona_a_cargo=forms.CharField(max_length=100)