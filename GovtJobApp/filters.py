import django_filters
from .models import *
class jobs_filter(django_filters.FilterSet):
    class Meta:
        model = BankJobs_model
        fields = ['location','age','qualification']

class railwayjob_filter(django_filters.FilterSet):
    class Meta:
        model = Railwayjobs_model
        fields = ['location','age','qualification']