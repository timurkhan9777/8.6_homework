from django.db import models

class Hudud(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField()
    hudud = models.ForeignKey(Hudud,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Building(models.Model):
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    hudud = models.ForeignKey(Hudud,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    field = models.IntegerField()
    floor = models.IntegerField()
    parking = models.BooleanField()
    playground = models.BooleanField()
    lift = models.BooleanField()

    def __str__(self):
        return self.name