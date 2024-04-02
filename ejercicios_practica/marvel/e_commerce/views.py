# Create your views here.
from django.http import JsonResponse
from e_commerce.models import Comic


def comic_list_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea
        print("Endpoint: comic_list_api_view")
        # traigo todos los comics a mi query
        queryset = Comic.objects.all()
        # convierto los valores de la query a dict y luego a list
        _data = list(queryset.values())
                # retorno un json
        return JsonResponse(data=_data, safe=False, status=200)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)


def comic_filter_stock_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea
        print("Endpoint: comic_filter_stock_api_view")
        # hago la query filtrada
        queryset = Comic.objects.filter(stock_qty=5)
        # serializo a lista de diccionarios
        _data = list(queryset.values())
        # retorno la data
        return JsonResponse(data=_data, safe=False, status=200)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)


def comic_filter_price_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea
        print("Endpoint: comic_filter_price_api_view")
        # mi query
        queryset = Comic.objects.filter(price__gt=3)
        # serializo
        _data = list(queryset.values())

        return JsonResponse(data=_data, safe=False, status=200)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)


def comic_list_order_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea
        print("Endpoint: comic_list_order_api_view")
        # query
        queryset = Comic.objects.all().order_by('marvel_id')
        # serialize
        _data = list(queryset.values())

        return JsonResponse(data=_data, safe=False, status=200)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)
