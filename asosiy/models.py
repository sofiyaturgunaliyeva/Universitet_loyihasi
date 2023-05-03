from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=50)
    aktiv = models.BooleanField()

    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom = models.CharField(max_length=50)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField()

    def __str__(self):
        return self.nom

class Ustoz(models.Model):
    jins_tanlov = [("Ayol","Ayol"),("Erkak","Erkak")]
    daraja_tanlov = [("Bakalavr","Bakalavr"),("Magistr","Magistr"),
                     ("Aspirant","Aspirant"),("Doktor","Doktor")
                     ]
    ism = models.CharField(max_length=50)
    yosh = models.SmallIntegerField()
    jins = models.CharField(max_length=50 , choices=jins_tanlov)
    daraja = models.CharField(max_length=50 , choices=daraja_tanlov)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


