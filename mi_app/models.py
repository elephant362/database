from django.db import models


class SensorData(models.Model):
    temperatura = models.FloatField()
    humedad = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.temperatura}°C, {self.humedad}% - {self.fecha}"
