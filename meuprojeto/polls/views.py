from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Página index do sistema de votação.')
