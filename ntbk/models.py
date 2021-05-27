import json
from django.db import models
from django.db.models import Value

# Create your models here.

class Rutina(models.Model):
    start  = models.DateTimeField('Inicio', auto_now_add = True)
    type   = models.CharField('Tipo', max_length=20)
    status = models.CharField('Estado', max_length=15)
    finish = models.CharField('Termino', max_length=50)
    items  = models.IntegerField('Items', default=0) 


    def __str__(self):
        output = str(self.start)
        return output
    def plus1Item(self):
        self.items = self.items + 1

def get_default_dict():
    return {'accept_list': [], 'reject_list': []}

class Note(models.Model):
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=100)
    img = models.CharField('img', max_length=100)
    bateria = models.CharField('Bateria', max_length=100)
    peso = models.CharField('Peso', max_length=100)
    pantalla = models.CharField('Pantalla', max_length=100)
    tasa_ref = models.CharField('Tasa Ref', max_length=100)
    proce = models.CharField('CPU', max_length=100)
    proce_nucleos = models.CharField('CPUNucleos', max_length=100)
    proce_hilos = models.CharField('CPUHilos', max_length=100)
    proce_freq = models.CharField('CPUFreq', max_length=100)
    proce_freq_turbo = models.CharField('CPUTurbo', max_length=100)
    gpu = models.CharField('GPU', max_length=100)
    gpuDedi = models.CharField('GPUDed', max_length=100)
    so = models.CharField('S.O.', max_length=100)
    almace = models.CharField('Almacenamiento', max_length=100)
    ram = models.CharField('RAM', max_length=100)
    ramint = models.IntegerField('RAM INT', default=0)
    puertos = models.CharField('Puertos', max_length=100)
    dimensiones = models.CharField('Dimen', max_length=100)
    aplicaciones = models.CharField('Aplicaciones', max_length=100)
    gamming = models.CharField('Gaming', max_length=100)
    movilidad = models.CharField('Movilidad', max_length=100)
    score_gpu = models.IntegerField('PuntajeGPU')
    score_cpu = models.IntegerField('PuntajeCPU')
    precio = models.CharField('Precio', max_length=50)
    precioint = models.IntegerField('PrecioInt', default=0)
    puntaje1 = models.IntegerField('Puntaje1', default=0)
    puntaje2 = models.IntegerField('Puntaje2', default=0)
    solotodo_id = models.CharField('ID Solotodo', max_length=51)
    dataj = models.JSONField(default=get_default_dict())

    #linksd

    def __str__(self):
        return self.nombre
    def name(self):
        return(self.nombre)
    def raminfo(self):
        return(self.ram)
    def imagenurl(self):
        return(self.img)
    def bateriainfo(self):
        return(self.bateria)
    def pesoinfo(self):
        return(str(self.peso) + 'g')
    def pantallainfo(self):
        return(self.pantalla + ' ' + self.tasa_ref) 
    def proceinfo(self):
        return(self.proce + ' (' + self.proce_nucleos + ' nucleos / ' + self.proce_hilos + ' hilos / '+ self.proce_frec + ' - ' + self.proce_frec_turbo + ')')
    def gpuinfo(self):
        return(self.gpu + '\n' + self.gpuDedi)
    def soinfo(self):
        return(self.so)
    def almacenamientoinfo(self):
        item = len(self.almacenamiento)
        if item == 2:
            return(self.almacenamiento[0] + '\n' + self.almacenamiento[1])
        return(self.almacenamiento[0])
    def puertosinfo(self):
        text= ''
        for x in range(len(self.puertos)):
            text = text + self.puertos[x] + '\n'
        return(text)
    def dimensionesinfo(self):
        return(self.dimensiones)
    def scoreApp(self):
        return(self.aplicaciones)
    def scoreGame(self):
        return(self.gaming)
    def scoreMov(self):
        return(self.movilidad)
    def scoreCpu(self):
        return(self.score_cpu)
    def scoreGpu(self):
        return(self.score_gpu)
    

    

