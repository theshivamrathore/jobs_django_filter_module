from django.contrib import admin
from .models import *
# Register your models here.

class BankJobs_admin(admin.ModelAdmin):
    list_display = ['bank_name','location','qualification','age','total_vacancies']

class Railwayjobs_admin(admin.ModelAdmin):
    list_display = ['position','location','qualification','age','total_vacancies']


admin.site.register(BankJobs_model,BankJobs_admin)
admin.site.register(Railwayjobs_model,Railwayjobs_admin)