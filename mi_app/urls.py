from django.contrib import admin
from django.urls import path, include
from mi_app.views import dashboard, obtener_datos_json #  Importa la vista del dashboard

urlpatterns = [
    path('', dashboard, name="dashboard"),  # This matches the root URL
    path('dashboard/', dashboard, name="dashboard"),
    path('', dashboard, name="home"),
    path('api/datos/', obtener_datos_json, name='api_datos'),  # Asegúrate de que esta ruta esté aquí

]