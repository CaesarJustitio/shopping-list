from django.forms import ModelForm
from main.models import Product

from django.shortcuts import redirect
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]