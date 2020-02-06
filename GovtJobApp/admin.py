from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class BankJobs_admin(admin.ModelAdmin):
    list_display = ['bank_name','location','qualification','age','total_vacancies']

class Railwayjobs_admin(admin.ModelAdmin):
    list_display = ['position','location','qualification','age','total_vacancies']

class Policejobs_admin(admin.ModelAdmin):
    list_display = ['position','location','qualification','age','total_vacancies']

class Forestjobs_admin(admin.ModelAdmin):
    list_display = ['id','position','location','qualification','age','total_vacancies']

@admin.register(BankJobs_model)
class view(ImportExportModelAdmin):
    pass

@admin.register(Railwayjobs_model)
class view(ImportExportModelAdmin):
    pass

@admin.register(Policejobs_model)
class view(ImportExportModelAdmin):
    pass

@admin.register(Forestjobs_model)
class view(ImportExportModelAdmin):
    pass

#admin.site.register(BankJobs_model,BankJobs_admin)
#admin.site.register(Railwayjobs_model,Railwayjobs_admin)
#admin.site.register(Policejobs_model,Policejobs_admin)