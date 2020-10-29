from django.shortcuts import render
from django.contrib.auth.forms import (
    UserCreationForm)
from django.urls import (
    reverse_lazy)
from django.views.genric import(
    CreateView
    )

class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = reverse_lazy(
        'core:MovieList')

# Create your views here.
