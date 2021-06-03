from django.shortcuts import render,HttpResponse
from core.models import Evento

# Create your views here.
def local_evento(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    if evento.local is None:
        local = 'Sem local definido'
    else:
        local = evento.local
    return HttpResponse(local)
