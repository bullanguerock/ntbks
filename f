[33mcommit 423554945c4a309b3b249dea919ca25c048d51f9[m[33m ([m[1;36mHEAD -> [m[1;32mdev[m[33m, [m[1;31mgithub/dev[m[33m)[m
Author: pcaynzec <toto.palacios.a@gmail.com>
Date:   Wed Jun 2 18:31:30 2021 -0400

    filter fixes

[1mdiff --git a/celerybeat-schedule.dat b/celerybeat-schedule.dat[m
[1mindex f38a448..5589252 100644[m
Binary files a/celerybeat-schedule.dat and b/celerybeat-schedule.dat differ
[1mdiff --git a/db.sqlitefix b/db.sqlitefix[m
[1mindex 406f30d..192c4d5 100644[m
Binary files a/db.sqlitefix and b/db.sqlitefix differ
[1mdiff --git a/ntbk/__pycache__/admin.cpython-38.pyc b/ntbk/__pycache__/admin.cpython-38.pyc[m
[1mindex 0c02b02..122aaad 100644[m
Binary files a/ntbk/__pycache__/admin.cpython-38.pyc and b/ntbk/__pycache__/admin.cpython-38.pyc differ
[1mdiff --git a/ntbk/__pycache__/filters.cpython-38.pyc b/ntbk/__pycache__/filters.cpython-38.pyc[m
[1mindex 3953071..25895c9 100644[m
Binary files a/ntbk/__pycache__/filters.cpython-38.pyc and b/ntbk/__pycache__/filters.cpython-38.pyc differ
[1mdiff --git a/ntbk/__pycache__/views.cpython-38.pyc b/ntbk/__pycache__/views.cpython-38.pyc[m
[1mindex 2f06f26..b8132b9 100644[m
Binary files a/ntbk/__pycache__/views.cpython-38.pyc and b/ntbk/__pycache__/views.cpython-38.pyc differ
[1mdiff --git a/ntbk/admin.py b/ntbk/admin.py[m
[1mindex 002d1ec..e891bc0 100644[m
[1m--- a/ntbk/admin.py[m
[1m+++ b/ntbk/admin.py[m
[36m@@ -1,4 +1,4 @@[m
[31m-from ntbk.models import Note, Rutina[m
[32m+[m[32mfrom .models import Note, Rutina[m
 from django.contrib import admin[m
 [m
 # Register your models here.[m
[1mdiff --git a/ntbk/filters.py b/ntbk/filters.py[m
[1mindex 4a1fa81..db36117 100644[m
[1m--- a/ntbk/filters.py[m
[1m+++ b/ntbk/filters.py[m
[36m@@ -2,13 +2,19 @@[m [mfrom django.db.models.fields import BooleanField[m
 from django.forms.widgets import Input, Select[m
 import django_filters[m
 from django_filters import widgets[m
[31m-from django_filters.filters import BooleanFilter, CharFilter , AllValuesFilter, NumberFilter , RangeFilter[m
[32m+[m[32mfrom django_filters.filters import BooleanFilter, CharFilter , AllValuesFilter, NumberFilter , RangeFilter, ChoiceFilter[m
 [m
 from .models import Note[m
 [m
 from django.db.models import Q[m
 [m
 [m
[32m+[m[32mFILTER_CHOICES = ([m
[32m+[m[32m    ('', 'Todos'),[m
[32m+[m[32m    ('GB', 'Gamer'),[m
[32m+[m[32m    ('No tar', 'Oficina')[m
[32m+[m[32m)[m
[32m+[m
 def multiple_search(queryset, name, value):[m
     queryset = queryset.filter([m
                                 Q(nombre__icontains=value) | [m
[36m@@ -22,13 +28,14 @@[m [mdef multiple_search(queryset, name, value):[m
 class NtbkFilter(django_filters.FilterSet):[m
 [m
     q = CharFilter(method=multiple_search, widget=Input(attrs={ 'type' : 'search',[m
[31m-                                                                'placeholder' : 'mm food...',[m
[32m+[m[32m                                                                'placeholder' : '...',[m
                                                                 'autocomplete' : 'off',[m
                                                                }))[m
     g = CharFilter(field_name='gpuDedi', lookup_expr='icontains')[m
     #ramint = CharFilter(field_name='ram', lookup_expr='icontains')[m
     ramint = AllValuesFilter(field_name='ramint', widget=Select(attrs={ 'class' : 'filter'}))[m
[31m-    precioRange = RangeFilter(field_name='precioint')[m
[32m+[m[32m    p = RangeFilter(field_name='precioint')[m
[32m+[m[32m    tipo = ChoiceFilter(field_name='gpuDedi', choices=FILTER_CHOICES, lookup_expr='icontains')[m
 [m
     class Meta:[m
         model = Note[m
[1mdiff --git a/ntbk/views.py b/ntbk/views.py[m
[1mindex de900e5..ce4b54d 100644[m
[1m--- a/ntbk/views.py[m
[1m+++ b/ntbk/views.py[m
[36m@@ -57,14 +57,14 @@[m [mdef testui(request):[m
 def testfilters(request):[m
     rutina = Rutina.objects.latest('id')[m
     n = Note.objects.filter(id_rutina = rutina)[m
[31m-    n1 = n.filter(ramint__range= (4,1024),puntaje2__range = (1,100000), score_cpu__range = (3600,1000000)).order_by('precioint')[m
[32m+[m[32m    n1 = n.filter(ramint__range= (4,1024),puntaje2__range = (1,100000), score_cpu__range = (1,1000000)).order_by('precioint')[m
 [m
     filtered_ntbks = NtbkFilter(request.GET, queryset=n1)[m
     [m
 [m
     paginated_filtered_ntbks = Paginator(filtered_ntbks.qs, 16)[m
     page_number = request.GET.get('page')[m
[31m-    ntbk_page_obj = paginated_filtered_ntbks.get_page(page_number)    [m
[32m+[m[32m    ntbk_page_obj = paginated_filtered_ntbks.get_page(page_number)[m[41m   [m
 [m
     return render(request, 'test_filters.html', {'ntbk_page_obj' : ntbk_page_obj ,[m
                                                  'filtered_ntbks' : filtered_ntbks ,[m
[1mdiff --git a/templates/test_filters.html b/templates/test_filters.html[m
[1mindex 3280183..90a5555 100644[m
[1m--- a/templates/test_filters.html[m
[1m+++ b/templates/test_filters.html[m
[36m@@ -66,12 +66,12 @@[m
 			<div class="cd-tab-filter">[m
 				<ul class="cd-filters">[m
 					<li class="placeholder"> [m
[31m-						<a data-type="all" href="#0">Todos</a> <!-- selected option on mobile -->[m
[32m+[m						[32m<a>Todos</a> <!-- selected option on mobile -->[m
 					</li> [m
[31m-					<li class="filter"><a class="selected" href="">Todos</a></li>[m
[31m-                    <!--[m
[31m-					<li class="filter" ><a href="" >Gamer</a></li>[m
[31m-					<li class="filter" ><a href="" >Oficina</a></li>-->[m
[32m+[m					[32m<li class="filter"><a class="selected" id="t" style="cursor:pointer;">Todos</a></li>[m
[32m+[m[41m                    [m
[32m+[m					[32m<li class="filter" ><a id="g" style="cursor:pointer;">Gamer</a></li>[m
[32m+[m					[32m<li class="filter" ><a id="o" style="cursor:pointer;">Oficina</a></li>[m
 				</ul> <!-- cd-filters -->[m
 			</div> <!-- cd-tab-filter -->[m
 		</div> <!-- cd-tab-filter-wrapper -->[m
[36m@@ -88,8 +88,10 @@[m
                         {{ ntbk.proce }}<br>[m
                         {{ ntbk.gpu }}<br>[m
                         {{ ntbk.gpuDedi }}<br>[m
[31m-                        {{ ntbk.ramint }}<br>[m
[31m-                        {{ ntbk.precio }}[m
[32m+[m[32m                        {{ ntbk.ram }}<br>[m
[32m+[m[32m                        {{ ntbk.precio }}<br>[m
[32m+[m[32m                        {{ ntbk.almace }} <br>[m
[32m+[m[32m                        {{ ntbk.puntaje2 }}[m
                         [m
                     </div>[m
                     <br><br>[m
[36m@@ -126,7 +128,7 @@[m
 [m
         <div class="cd-filter">[m
             [m
[31m-            <form metohd='get'>[m
[32m+[m[32m            <form metohd='get' id="form-id">[m
 [m
                 <div class="cd-filter-block">[m
                     <h4>Precio</h4>[m
[36m@@ -134,12 +136,12 @@[m
                     <br>[m
                     <div class="cd-filter-content">[m
                         <div id="slider"></div>[m
[31m-                        <input type="hidden" name="precioRange_min" id="id_precioRange_0">[m
[31m-                        <input type="hidden" name="precioRange_max" id="id_precioRange_1">[m
[32m+[m[32m                        <input type="hidden" name="p_min" id="id_p_0">[m
[32m+[m[32m                        <input type="hidden" name="p_max" id="id_p_1">[m
                     </div>[m
                 </div>[m
 [m
[31m-                {# filtered_ntbks.form.as_p #}[m
[32m+[m[41m                [m
                 <div class="cd-filter-block">[m
                     <h4>Busqueda</h4>[m
                     <div class="cd-filter-content">[m
[36m@@ -155,9 +157,27 @@[m
                         </div>[m
                     </div>                    [m
                 </div>[m
[32m+[m
[32m+[m[32m                <div class="cd-filter-block" hidden>[m
[32m+[m[32m                    <h4>Tipo</h4>[m
[32m+[m[32m                    <div class="cd-filter-content">[m
[32m+[m[32m                        <div class="cd-select cd-filters">[m
[32m+[m[32m                            <select name="tipo" id="id_tipo" hidden>[m
[32m+[m[32m                                <option value="">---------</option>[m
[32m+[m[41m                              [m
[32m+[m[32m                                <option value="">Todos</option>[m
[32m+[m[41m                              [m
[32m+[m[32m                                <option value="GB">Gamer</option>[m
[32m+[m[41m                              [m
[32m+[m[32m                                <option value="No tar" selected="">Oficina</option>[m
[32m+[m[41m                              [m
[32m+[m[32m                              </select>[m
[32m+[m[32m                        </div>[m
[32m+[m[32m                    </div>[m[41m                    [m
[32m+[m[32m                </div>[m
                 [m
 [m
[31m-                <input type="submit" value="Press">[m
[32m+[m[32m                <input type="submit" value="Filtrar">[m
                 <br>[m
                                 [m
 [m
[36m@@ -254,8 +274,10 @@[m
     </script>[m
     <script>[m
         var slider = document.getElementById('slider');[m
[31m-        var inicio = 100000[m
[31m-        var fin = 1000000[m
[32m+[m[41m        [m
[32m+[m[32m        var inicio = 100000;[m
[32m+[m[32m        var fin = 1000000;[m
[32m+[m[41m        [m
         if (localStorage.getItem("preciomin") && localStorage.getItem("preciomax")){[m
             inicio = localStorage.getItem("preciomin")[m
             fin = localStorage.getItem("preciomax")[m
[36m@@ -264,7 +286,7 @@[m
         noUiSlider.create(slider, {[m
             start: [inicio, fin],[m
             behaviour: 'drag-tap',[m
[31m-            tooltips: [true, true],[m
[32m+[m[32m            tooltips: [true, true],[m[41m [m
             format: wNumb({[m
                 decimals: 0,[m
                 thousand: '.',[m
[36m@@ -284,17 +306,63 @@[m
 [m
         slider.noUiSlider.on('update', function (values) {[m
             var handleValue = slider.noUiSlider.get();[m
[31m-            id_precioRange_0.value = handleValue[0].replace(/\D/g,'');[m
[31m-            localStorage.setItem("preciomin",id_precioRange_0.value);[m
[32m+[m[32m            id_p_0.value = handleValue[0].replace(/\D/g,'');[m
[32m+[m[32m            localStorage.setItem("preciomin",id_p_0.value);[m
                  [m
 [m
[31m-            id_precioRange_1.value = handleValue[1].replace(/\D/g,'');[m
[31m-            localStorage.setItem("preciomax", id_precioRange_1.value);[m
[32m+[m[32m            id_p_1.value = handleValue[1].replace(/\D/g,'');[m
[32m+[m[32m            localStorage.setItem("preciomax", id_p_1.value);[m
             [m
         });[m
         [m
         mergeTooltips(slider, 100, ' - ');[m
     </script>[m
[32m+[m[32m    <script>[m[41m    [m
[32m+[m
[32m+[m[32m        var gamer = document.getElementById("g");[m
[32m+[m[32m        var todos = document.getElementById("t");[m
[32m+[m[32m        var oficina = document.getElementById("o");[m
[32m+[m
[32m+[m[32m        var target = document.getElementById("id_tipo");[m
[32m+[m
[32m+[m[32m        if (localStorage.getItem("selected") == 't'){[m
[32m+[m[32m            gamer.classList.remove("selected");[m
[32m+[m[32m            todos.classList.add("selected");[m
[32m+[m[32m            oficina.classList.remove("selected");[m
[32m+[m[32m            target.value = '';[m
[32m+[m[32m        } else if (localStorage.getItem("selected") == 'g'){[m
[32m+[m[32m            gamer.classList.add("selected");[m
[32m+[m[32m            todos.classList.remove("selected");[m
[32m+[m[32m            oficina.classList.remove("selected");[m
[32m+[m[32m            target.value = 'GB';[m
[32m+[m[32m        } else if (localStorage.getItem("selected") == 'o'){[m
[32m+[m[32m            gamer.classList.remove("selected");[m
[32m+[m[32m            todos.classList.remove("selected");[m
[32m+[m[32m            oficina.classList.add("selected");[m
[32m+[m[32m            target.value = 'No tar';[m
[32m+[m[32m        }[m
[32m+[m[41m        [m
[32m+[m[41m        [m
[32m+[m
[32m+[m[32m        var form = document.getElementById("form-id");[m
[32m+[m[41m        [m
[32m+[m[32m        gamer.addEventListener("click", function () {[m
[32m+[m[32m            localStorage.setItem("selected",'g');[m
[32m+[m[32m            target.value = 'GB';[m
[32m+[m[32m            form.submit();[m
[32m+[m[32m        });[m
[32m+[m[32m        oficina.addEventListener("click", function () {[m
[32m+[m[32m            localStorage.setItem("selected",'o');[m
[32m+[m[32m            target.value = 'No tar';[m
[32m+[m[32m            form.submit();[m
[32m+[m[32m        });[m
[32m+[m[32m        todos.addEventListener("click", function () {[m
[32m+[m[32m            localStorage.setItem("selected",'t');[m
[32m+[m[32m            target.value = '';[m
[32m+[m[32m            form.submit();[m
[32m+[m[32m        });[m
[32m+[m
[32m+[m[32m    </script>[m
     [m
 </body>[m
 </html>[m
\ No newline at end of file[m
