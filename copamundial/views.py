from django.shortcuts import render
from copamundial.models import Selecciones
from copamundial.models import Grupos
# Create your views here.
def selecciones(request):

    team = Selecciones.objects.all()
    return render(request,'equipos.html', context={'team': team})


def grupos(request):

    group = Grupos.objects.all()
    return render(request,'grupos.html', context={'group':group})