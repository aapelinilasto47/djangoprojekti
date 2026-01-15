from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tuote(models.Model):
    ean_koodi = models.CharField(max_length=13, unique=True, primary_key=True)
    nimi = models.CharField(max_length=100)
    kuva = models.CharField(max_length=200, blank=True)

class Varastot(models.Model):
    varasto_id = models.AutoField(primary_key=True)
    ean_koodi = models.ForeignKey(Tuote, on_delete=models.CASCADE)
    
    kayttaja = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    sijainti = models.CharField(max_length=100, choices=[('jääkaappi', 'Jääkaappi'), ('pakastin', 'Pakastin'), ('kuivakaappi', 'Kuivakaappi')], default='kuivakaappi')
    määrä = models.IntegerField()
    ostopäivä = models.DateField()
    viimeinen_käyttöpäivä = models.DateField()

