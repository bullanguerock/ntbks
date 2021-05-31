from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import Note, Rutina

from .filters import NtbkFilter

from django.core.paginator import Paginator


#ajax test
from django.views.generic import TemplateView
from django.http import HttpResponse

import json

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

#TEST Filters
def testfilters(request):
    rutina = Rutina.objects.latest('id')
    n = Note.objects.filter(id_rutina = rutina)
    n1 = n.filter(ramint__range= (6,1000),puntaje2__range = (1,100), score_cpu__range = (3600,1000000)).order_by('precioint')

    filtered_ntbks = NtbkFilter(request.GET, queryset=n1)

    paginated_filtered_ntbks = Paginator(filtered_ntbks.qs, 16)
    page_number = request.GET.get('page')
    ntbk_page_obj = paginated_filtered_ntbks.get_page(page_number)    

    return render(request, 'test_filters.html', {'ntbk_page_obj' : ntbk_page_obj ,
                                                 'filtered_ntbks' : filtered_ntbks ,
                                                })

#ajax test
def main_view(request):
    rutina = Rutina.objects.latest('id')
    n = Note.objects.filter(id_rutina = rutina)
    n1 = n.filter(ramint__range= (4,1000),puntaje2__range = (1,100), score_cpu__range = (3600,1000000)).order_by('precioint')

    filtered_ntbks = NtbkFilter(request.GET, queryset=n1)

    paginated_filtered_ntbks = Paginator(filtered_ntbks.qs, 20)
    page_number = request.GET.get('page')
    ntbk_page_obj = paginated_filtered_ntbks.get_page(page_number)    

    return render(request, 'ntbks.html', {'ntbk_page_obj' : ntbk_page_obj ,
                                          'filtered_ntbks' : filtered_ntbks ,
                                        })

#def search_results(request):
    if request.is_ajax():
        game = request.POST.get('game')
        rutina = Rutina.objects.latest('id')
        qs = Note.objects.filter(id_rutina = rutina, puntaje2__range=(1, 60), nombre__icontains=game)
        
        if len(qs) > 0 and len(game) > 0:
            data = []
            for pos in qs:
                item = {
                    'pk' : pos.pk,
                    'nombre' : pos.nombre,
                    'img' : pos.img,
                    'precio' : pos.precio,
                }
                data.append(item)
            res = data
        else:
            res = 'No games found...'
        return JsonResponse({'data' : res})
    return JsonResponse({})

def search_results(request):
    if request.is_ajax():
        query = request.POST.get('query')
        ram = request.POST.get('ram')
        red = "?q="+query+"&ram="+ram
        json = {"redirect" : True,
                "redirect_url": red ,
                "keepram" : ram,
                "keepq" : query,
               }
        return JsonResponse(json)
    return JsonResponse({})


    

