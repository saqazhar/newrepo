from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mynewapp.models import myform
# Create your views here.

class MyFormList(ListView):
    model = myform

class MyFormDetail(DetailView):
    model = myform

class MyFormCreate(CreateView):
    model = myform
    fields = ['name','email','address']

class MyFormUpdate(UpdateView):
    model = myform
    fields = ['name','email','address']

class MyFormDelete(DeleteView):
    model = myform