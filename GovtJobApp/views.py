from django.shortcuts import render
from .models import BankJobs_model
from .filters import *
from django.http.response import HttpResponse
# Create your views here.

def index_view(request):
    return render(request,'GovtJobApp/index.html')

def govtjobs_home_view(request):
    return render(request,'GovtJobApp/govtjob_home.html')

def bankjobs_details_view(request):
    bank_data = BankJobs_model.objects.all()
    return render(request,'GovtJobApp/bank_jobs.html', {'bank_data':bank_data})

def filter_view(request):
    f=jobs_filter(request.GET,queryset=BankJobs_model.objects.all())
    return render(request,'GovtJobApp/filter.html',{'f':f})


# Railway Views starts here #
def railwayjob_view(request):
    railway_data = railwayjob_filter(request.GET,queryset=Railwayjobs_model.objects.all())
    return render(request, 'GovtJobApp/railwayjobs_details.html', {'railway_data':railway_data})
# Railway Views starts here #


