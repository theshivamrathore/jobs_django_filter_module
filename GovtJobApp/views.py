from django.shortcuts import render
from .models import *
from .filters import *
from .forms import *

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

def policejob_view(request):
    if request.method=="POST":
        featured_data = request.POST.get('dropdown')
        featured_data1 = request.POST.get('dropdown')
        listings = Policejobs_model.objects.filter(location=featured_data)   #qualification=featured_data1 (only one comming location or qualification)
        print(listings)
    else:
        listings = Policejobs_model.objects.all()

    return render(request,'GovtJobApp/policejobs_details.html',{'listings':listings})



def forestjob_view(request):
    # data = Forestjobs_model.objects.all()
    if request.method=="POST":
        fform = ForestDropdownForm(request.POST)
        if fform.is_valid():
            location = request.POST.get('select')
            qualification = request.POST.get('select_qualification')
            age = request.POST.get('age')
            # data = Forestjobs_model.objects.all().filter(location=location,qualification=qualification)
            data = Forestjobs_model.objects.filter(location=location,qualification=qualification,age=age)
        else:
            return HttpResponse('some filed missed')
    else:
        fform = ForestDropdownForm()
        data = Forestjobs_model.objects.all()
    return render(request,'GovtJobApp/forestjob_details.html',{'fform':fform,'data':data})




