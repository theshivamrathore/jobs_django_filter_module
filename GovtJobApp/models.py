from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class BankJobs_model(models.Model):
    bank_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    qualification = models.CharField(max_length=10)
    age = models.IntegerField()
    total_vacancies = models.IntegerField()

    def __str__(self):
        return self.bank_name

class Railwayjobs_model(models.Model):
    position = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    qualification = models.CharField(max_length=10)
    age = models.IntegerField()
    total_vacancies = models.IntegerField()

class Policejobs_model(models.Model):
    position = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    qualification = models.CharField(max_length=10)
    age = models.IntegerField()
    total_vacancies = models.IntegerField()

class Forestjobs_model(models.Model):
    position = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    qualification = models.CharField(max_length=10)
    age = models.IntegerField()
    total_vacancies = models.IntegerField()

    def __str__(self):
        return self.position


