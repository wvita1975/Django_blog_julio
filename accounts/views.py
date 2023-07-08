from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/sing_up.html'