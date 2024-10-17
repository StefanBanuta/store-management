from django.db import models

class Client(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    adresa = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nume} {self.prenume}"

class ProdusAlimentar(models.Model):
    denumire = models.CharField(max_length=100)
    data_producere = models.DateField()
    data_expirare = models.DateField()

    def __str__(self):
        return self.denumire

class Achizitie(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produs = models.ForeignKey(ProdusAlimentar, on_delete=models.CASCADE)
    data_achizitie = models.DateTimeField()

    def __str__(self):
        return f"Achizitie {self.client} - {self.produs} la {self.data_achizitie}"

class Producator(models.Model):
    denumire = models.CharField(max_length=45)
    tara_origine = models.CharField(max_length=60)
    adresa = models.CharField(max_length=60)
    
    def __str__(self):
        return self.denumire


class Comanda(models.Model):
    produs = models.ForeignKey(ProdusAlimentar, on_delete=models.CASCADE)
    producator = models.ForeignKey(Producator, on_delete=models.CASCADE)
    data_comanda = models.DateTimeField()


