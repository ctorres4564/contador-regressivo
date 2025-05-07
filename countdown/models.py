from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    def clean(self):
        # Verificar se a data é no futuro
        if self.date and self.date <= datetime.now():
            raise ValidationError({'date': 'A data do evento deve ser no futuro.'})
