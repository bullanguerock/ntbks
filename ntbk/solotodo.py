import json
import requests
from .models import Note


def get_api_info(id_prod, id_rut):
    r = requests.get('https://publicapi.solotodo.com/products/' + id_prod)
    data = r.json()
    n = Note(id_rutina = id_rut)
    n.nombre = data['name']
    n.img = data['picture_url']
    n.bateria = data['specs']['pretty_battery']
    n.peso = data['specs']['weight']
    n.pantalla = data['specs']['screen_unicode']
    n.tasa_ref = data['specs']['screen_refresh_rate_unicode']
    n.proce = data['specs']['processor_unicode']
    n.proce_nucleos = data['specs']['processor_core_count_unicode']
    n.proce_hilos = data['specs']['processor_thread_count_unicode']
    n.proce_frec = data['specs']['processor_frequency_unicode']
    n.proce_frec_turbo = data['specs']['processor_turbo_frequency_unicode']
    try:
        n.gpu = data['specs']['processor_gpu_unicode']
    except:
        n.gpu = 'No info/tiene tarjeta de video integrada'
        print('no gpu integrada')
    try:
        n.gpuDedi = data['specs']['dedicated_video_card_unicode']
    except:
        n.gpuDedi = 'No tarjeta de video dedicada'
        print('no gpu dedicada')
    n.so = data['specs']['operating_system_unicode']
    n.almace = data['specs']['storage_drive_unicode']
    n.ram = data['specs']['pretty_ram']
    n.puertos = data['specs']['ports_unicode']
    n.dimensiones = data['specs']['pretty_dimensions']
    n.aplicaciones = data['specs']['score_general']
    n.gamming = data['specs']['score_games']
    n.movilidad = data['specs']['score_mobility']
    try:
        n.score_gpu = data['specs']['processor_gpu_speed_score']
    except:
        n.score_gpu = 0
        print('no scoreGPU')
    try:
        n.score_cpu = data['specs']['processor_speed_score']
    except:
        n.score_cpu = 0
        print('no scoreCPU')
    n.save()
    return n










#class Producto:
#    def __init__(self, id_prod):
#        r = requests.get('https://publicapi.solotodo.com/products/' + id_prod)
#        data = r.json()
#        self.nombre = data['name']
#        self.img = data['picture_url']
#        self.bateria = data['specs']['pretty_battery']
#        self.peso = data['specs']['weight']
#        self.pantalla = data['specs']['screen_unicode']
#        self.tasa_ref = data['specs']['screen_refresh_rate_unicode']
#        self.proce = data['specs']['processor_unicode']
#        self.proce_nucleos = data['specs']['processor_core_count_unicode']
#        self.proce_hilos = data['specs']['processor_thread_count_unicode']
#        self.proce_frec = data['specs']['processor_frequency_unicode']
#        self.proce_frec_turbo = data['specs']['processor_turbo_frequency_unicode']
#        try:
#            self.gpu = data['specs']['processor_gpu_unicode']
#        except:
#            self.gpu = 'No tarjeta de video integrada'
#            print('no gpu integrada')
#        try:
#            self.gpuDedi = data['specs']['dedicated_video_card_unicode']
#        except:
#            self.gpuDedi = 'No tarjeta de video dedicada'
#            print('no gpu dedicada')
#        self.so = data['specs']['operating_system_unicode']
#        self.almacenamiento = data['specs']['storage_drive_unicode']
#        self.ram = data['specs']['pretty_ram']
#        self.puertos = data['specs']['ports_unicode']
#        self.dimensiones = data['specs']['pretty_dimensions']
#        self.aplicaciones = data['specs']['score_general']
#        self.gaming = data['specs']['score_games']
#        self.movilidad = data['specs']['score_mobility']
#        try:
#            self.score_gpu = data['specs']['processor_gpu_speed_score']
#        except:
#            self.score_gpu = 0
#            print('no scoregpu')
#        self.score_cpu = data['specs']['processor_speed_score']
#
#    def name(self):
#        return(self.nombre)
#    def raminfo(self):
#        return(self.ram)
#    def imagenurl(self):
#        return(self.img)
#    def bateriainfo(self):
#        return(self.bateria)
#    def pesoinfo(self):
#        return(str(self.peso) + 'g')
#    def pantallainfo(self):
#        return(self.pantalla + ' ' + self.tasa_ref) 
#    def proceinfo(self):
#        return(self.proce + ' (' + self.proce_nucleos + ' nucleos / ' + self.proce_hilos + ' hilos / '+ self.proce_frec + ' - ' + self.proce_frec_turbo + ')')
#    def gpuinfo(self):
#        return(self.gpu + '\n' + self.gpuDedi)
#    def soinfo(self):
#        return(self.so)
#    def almacenamientoinfo(self):
#        item = len(self.almacenamiento)
#        if item == 2:
#            return(self.almacenamiento[0] + '\n' + self.almacenamiento[1])
#        return(self.almacenamiento[0])
#    def puertosinfo(self):
#        text= ''
#        for x in range(len(self.puertos)):
#            text = text + self.puertos[x] + '\n'
#        return(text)
#    def dimensionesinfo(self):
#        return(self.dimensiones)
#    def scoreApp(self):
#        return(self.aplicaciones)
#    def scoreGame(self):
#        return(self.gaming)
#    def scoreMov(self):
#        return(self.movilidad)
#    def scoreCpu(self):
#        return(self.score_cpu)
#    def scoreGpu(self):
#        return(self.score_gpu)