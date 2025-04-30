from django.db import models
from django.db.transaction import mark_for_rollback_on_error
from django.core.validators import MaxValueValidator, MinValueValidator


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=155)
    kurs = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)], default=1
    )
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.ism)

class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    jins = models.CharField(choices=(("Erkak", "Erkak"), ("Ayol", "Ayol")))
    tugilgan_sana = models.DateField(blank=True, null=True)
    kitob_soni = models.PositiveSmallIntegerField(default=1)
    tirik = models.BooleanField(default=True)

    def __str__(self):
        return self.ism
class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=55)
    sahifa = models.PositiveSmallIntegerField(blank=True, null=True)
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nom

class Admin(models.Model):
    ism = models.CharField(max_length=255)
    ish_vaqti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.SET_NULL, blank=True, null=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, blank=True, null=True)
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, blank=True, null=True)
    olingan_sana = models.DateField(auto_now_add=True)
    qaytarish_sana = models.DateField()
    qaytarilgan = models.BooleanField(null=True)

    def __str__(self):
        return str(self.talaba)
