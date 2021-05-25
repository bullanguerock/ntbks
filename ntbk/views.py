from django.shortcuts import redirect, render
from .models import Note, Rutina

# Create your views here.
    

def index(request):
    presupuesto = 1000000
    rutina = Rutina.objects.latest('id')
    n = Note.objects.filter(id_rutina = rutina) 

    if request.method == 'POST':
        presupuesto = request.POST.get('presupuesto')
        servicio = request.POST.get('servicio')
        if servicio == 'gamer':
            n1 = n.exclude(gpuDedi__startswith='No ')
            n2 = n1.filter(precioint__range =(0,presupuesto)).order_by('puntaje2')
            return render(request, 'index.html',{'notes' : n2})
        
        elif servicio == 'ofimatica':   
            n1 = n.filter(gpuDedi__startswith='No ')          
            n2 = n1.filter(puntaje2__range=(1, 55), precioint__range =(0,presupuesto)).order_by('puntaje2')
            return render(request, 'index.html',{'notes' : n2})
            

    else:
        n1 = n.filter(puntaje2__range=(1, 60), precioint__range =(0,0)).order_by('puntaje2')     
  
    return render(request, 'index.html',{'notes' : n1})

    
