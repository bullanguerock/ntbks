import json
import requests
from .models import Note


def get_api_info(id_prod, id_rut):
    r = requests.get('https://publicapi.solotodo.com/products/' + id_prod)
    data = r.json()
    if data:
        n = Note(id_rutina = id_rut)
        n.dataj = data
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
        n.ramint = data['specs']['ram_quantity_value']
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
    return
