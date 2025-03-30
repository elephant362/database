from django.contrib import admin
from .models import SensorData

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('temperatura', 'humedad', 'fecha')  # Mostrar estos campos en la lista
    list_filter = ('fecha',)  # Permitir filtrar por fecha
    search_fields = ('temperatura', 'humedad')  # Hacer que sea posible buscar por temperatura o humedad
    ordering = ('-fecha',)  # Ordenar por la fecha de forma descendente
    date_hierarchy = 'fecha'  # Mostrar una jerarquía de fechas

admin.site.register(SensorData, SensorDataAdmin)
