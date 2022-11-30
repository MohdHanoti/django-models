from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Snack
# Create your views here.
class HomePage(TemplateView):

    template_name='home.html'

class AboutPage(TemplateView):

    template_name='about.html'

class ThingListView(ListView):
    template_name='snacks.html'
    model=Snack
    