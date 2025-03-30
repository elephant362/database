from django.shortcuts import render
from django.http import JsonResponse
from .models import SensorData

def obtener_datos_json(request):
    # Obtener los últimos 10 registros
    datos = SensorData.objects.all().order_by('-fecha')[:10]  
    # Convertir los datos a un formato adecuado para JSON
    datos_json = list(datos.values('temperatura', 'humedad', 'fecha'))
    return JsonResponse(datos_json, safe=False)
def dashboard(request):
    return render(request, "dashboard.html")
