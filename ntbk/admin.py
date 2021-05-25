from ntbk.models import Note, Rutina
from django.contrib import admin

# Register your models here.


@admin.register(Rutina)
class Rutinaadmin(admin.ModelAdmin):
    date_hierarchy = 'start'
    list_display = ('id','start', 'type', 'status', 'items', 'finish')
    list_filter = ['status', 'type']

@admin.register(Note)
class Noteadmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'puntaje1', 'puntaje2', 'proce','gpu','gpuDedi','ram', 'precioint', 'precio', 'id_rutina')
    list_filter = ['id_rutina']
    search_fields = ['proce']