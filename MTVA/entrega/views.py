from django.shortcuts import render
from entrega.models import Familiar
# Create your views here.
def familiares(request):

    familiar=Familiar.objects.all()

    contexto = {'familiares':familiar}

    return render(request, 'Familiares.html', contexto)