from django.shortcuts import redirect, render
from .models import Note, Rutina

# Create your views here.
    
# PRINCIPAL
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
            return render(request, 'index.html',{'notes' : n2,
                                                 'presu' : presupuesto, 
                                                }) 
        
        elif servicio == 'ofimatica':   
            n1 = n.filter(gpuDedi__startswith='No ')          
            n2 = n1.filter(puntaje2__range=(1, 55), precioint__range =(0,presupuesto)).order_by('puntaje2')
            return render(request, 'index.html', {'notes' : n2, 
                                                  'selected' : 'si',
                                                  'presu' : presupuesto 
                                                  })            

    else:
        n1 = n.filter(puntaje2__range=(1, 60), precioint__range =(0,0)).order_by('puntaje2')     
  
    return render(request, 'index.html',{'notes' : n1})

#TEST UI
def testui(request):
    rutina = Rutina.objects.latest('id')
    titulo = 'k fuentes'
    n = Note.objects.filter(id_rutina = rutina)
    n1 = n.filter(ramint__range= (6,1000),puntaje2__range = (1,100), score_cpu__range = (3600,1000000)).order_by('precioint')

    return render(request, 'ui.html', {'obj' : n1})

    

