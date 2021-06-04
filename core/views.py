from django.shortcuts import redirect, render,HttpResponse
from core.models import Evento

# Create your views here.
def local_evento(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    if evento.local is None:
        local = 'Sem local definido'
    else:
        local = evento.local
    return HttpResponse(local)

def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos}
    return render(request, 'agenda.html', dados)

#def index(request):
#    return redirect('/agenda/')