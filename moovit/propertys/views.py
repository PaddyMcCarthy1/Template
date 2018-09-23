from django.views import generic
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Property
from django.shortcuts import render


# Create your views here.


class PropertyListView(generic.ListView):
    model = Property

    def get_queryset(self):
        return Property.objects.order_by('-publish_date')
