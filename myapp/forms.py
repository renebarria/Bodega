from django import forms
from .models import Product

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description=forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))
    

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyect", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'input'}),
            'quantity': forms.NumberInput(attrs={'class': 'input'}),
        }


class CreateNewProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'input'}),
            'quantity': forms.NumberInput(attrs={'class': 'input'}),
        }

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'input'}),
            'quantity': forms.NumberInput(attrs={'class': 'input'}),
        }



