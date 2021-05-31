warning: LF will be replaced by CRLF in static/js/main.js.
The file will have its original line endings in your working directory
[1mdiff --git a/ntbk/__pycache__/filters.cpython-38.pyc b/ntbk/__pycache__/filters.cpython-38.pyc[m
[1mindex 7ae024c..d7da371 100644[m
Binary files a/ntbk/__pycache__/filters.cpython-38.pyc and b/ntbk/__pycache__/filters.cpython-38.pyc differ
[1mdiff --git a/ntbk/__pycache__/urls.cpython-38.pyc b/ntbk/__pycache__/urls.cpython-38.pyc[m
[1mindex b586d04..4582775 100644[m
Binary files a/ntbk/__pycache__/urls.cpython-38.pyc and b/ntbk/__pycache__/urls.cpython-38.pyc differ
[1mdiff --git a/ntbk/__pycache__/views.cpython-38.pyc b/ntbk/__pycache__/views.cpython-38.pyc[m
[1mindex 5a49117..4739142 100644[m
Binary files a/ntbk/__pycache__/views.cpython-38.pyc and b/ntbk/__pycache__/views.cpython-38.pyc differ
[1mdiff --git a/ntbk/filters.py b/ntbk/filters.py[m
[1mindex ae73ee6..a558c26 100644[m
[1m--- a/ntbk/filters.py[m
[1m+++ b/ntbk/filters.py[m
[36m@@ -1,11 +1,25 @@[m
[32m+[m[32mfrom django.db.models.fields import BooleanField[m
 import django_filters[m
[31m-from django_filters.filters import CharFilter[m
[32m+[m[32mfrom django_filters.filters import BooleanFilter, CharFilter[m
 [m
 from .models import Note[m
 [m
[32m+[m[32mfrom django.db.models import Q[m
[32m+[m
[32m+[m[32mdef multiple_search(queryset, name, value):[m
[32m+[m[32m    queryset = queryset.filter([m
[32m+[m[32m                                Q(nombre__icontains=value) |[m[41m [m
[32m+[m[32m                                Q(proce__icontains=value) |[m
[32m+[m[32m                                Q(gpu__icontains=value) |[m
[32m+[m[32m                                Q(gpuDedi__icontains=value) |[m
[32m+[m[32m                                Q(ram__icontains=value)[m
[32m+[m[32m                              )[m
[32m+[m[32m    return queryset[m
[32m+[m
 class NtbkFilter(django_filters.FilterSet):[m
 [m
[31m-    nombre = CharFilter(field_name='nombre', lookup_expr='icontains')[m
[32m+[m[32m    q = CharFilter(method=multiple_search)[m
[32m+[m[32m    g = CharFilter(field_name='gpuDedi', lookup_expr='icontains')[m
 [m
     class Meta:[m
         model = Note[m
[1mdiff --git a/ntbk/urls.py b/ntbk/urls.py[m
[1mindex c0c77d1..0ed171e 100644[m
[1m--- a/ntbk/urls.py[m
[1m+++ b/ntbk/urls.py[m
[36m@@ -5,6 +5,6 @@[m [murlpatterns = [[m
     path('', testui),[m
     path('test', index),[m
     path('filters', testfilters),[m
[31m-    path('ajax', main_view),[m
[31m-    path('ajax/search/', search_results),[m
[32m+[m[32m    path('ntbks', main_view),[m
[32m+[m[32m    path('ntbks/search/', search_results),[m
 ][m
\ No newline at end of file[m
[1mdiff --git a/ntbk/views.py b/ntbk/views.py[m
[1mindex c041fad..f62e97f 100644[m
[1m--- a/ntbk/views.py[m
[1m+++ b/ntbk/views.py[m
[36m@@ -71,12 +71,25 @@[m [mdef testfilters(request):[m
 [m
 #ajax test[m
 def main_view(request):[m
[31m-    return render(request, 'start.html', {})[m
[32m+[m[32m    rutina = Rutina.objects.latest('id')[m
[32m+[m[32m    n = Note.objects.filter(id_rutina = rutina)[m
[32m+[m[32m    n1 = n.filter(ramint__range= (4,1000),puntaje2__range = (1,100), score_cpu__range = (3600,1000000)).order_by('precioint')[m
 [m
[31m-def search_results(request):[m
[32m+[m[32m    filtered_ntbks = NtbkFilter(request.GET, queryset=n1)[m
[32m+[m
[32m+[m[32m    paginated_filtered_ntbks = Paginator(filtered_ntbks.qs, 20)[m
[32m+[m[32m    page_number = request.GET.get('page')[m
[32m+[m[32m    ntbk_page_obj = paginated_filtered_ntbks.get_page(page_number)[m[41m    [m
[32m+[m
[32m+[m[32m    return render(request, 'ntbks.html', {'ntbk_page_obj' : ntbk_page_obj ,[m
[32m+[m[32m                                          'filtered_ntbks' : filtered_ntbks ,[m
[32m+[m[32m                                        })[m
[32m+[m
[32m+[m[32m#def search_results(request):[m
     if request.is_ajax():[m
         game = request.POST.get('game')[m
[31m-        qs = Note.objects.filter(puntaje2__range=(1, 60), nombre__icontains=game)[m
[32m+[m[32m        rutina = Rut