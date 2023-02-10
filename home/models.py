from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)

class qordata(models.Model):
    x_axis=models.DateField()
    y_axis=models.IntegerField()

class qordata2(models.Model):
    x_axis=models.DateField()
    y_axis=models.IntegerField()

class qordata3(models.Model):
    x_axis=models.DateField()
    y_axis=models.IntegerField()

class qordata4(models.Model):
    suites=models.CharField(max_length=122)