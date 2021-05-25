from .solotodo import get_api_info
import requests
from bs4 import BeautifulSoup
import re
import json
from .models import Note, Rutina

def RutinaNotebooks():
    #rutina
    r = Rutina()
    r.type = 'Notebooks'
    r.status = 'Iniciado'
    r.save()


    #numero de paginas
    req = requests.get('https://www.solotodo.cl/notebooks?ordering=-score_general&page=1&')
    soup = BeautifulSoup(req.text, "lxml")
    html = soup.find_all("li", class_="page-item")
    pages = html[6].text
    print(pages)

    # ID, Precio, Puntaje Notebooks solotodo.cl

    limit=int(pages)+1
    count = 0

    r.status = 'Pendiente'
    r.save()
    #for recorre paginas
    for x in range (1,limit):
        req = requests.get('https://www.solotodo.cl/notebooks?ordering=-score_general&page='+str(x)+'&')
        soup = BeautifulSoup(req.text, "lxml")
        #for recorre 'targetas/items' de la pagina
        for link in soup.find_all("div", class_="price flex-grow"):
            #encontrar id
            tostr = str(link)
            try:
                found = re.search('/products/(.+?)-', tostr).group(1)
            except AttributeError:
                found = 'error' # apply your error handling

            #encontrar precio 
            precio = link.get_text()
            
            #guardar Api Info
            p=get_api_info(str(found), r)

            #calcular puntajes
            precioint = int(re.sub(r"\D", "", precio))
            puntaje = (p.scoreCpu() + p.scoreGpu())
            try:
                puntaje2 = precioint / puntaje
            except:
                puntaje2 = "0"

            #guardar precio, puntaje, idsolotodo
            p.solotodo_id = found
            p.precio = precio
            p.precioint = precioint
            p.puntaje1 = puntaje
            p.puntaje2 = puntaje2
            p.save()
            r.plus1Item()
            r.save()
            
        
        count = count + 1
    print(count)
    r.status = 'Finalizado'
    #r.finish = DateTimeField(auto_now_add=True)
    r.save()


