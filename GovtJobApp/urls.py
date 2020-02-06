"""JobProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from GovtJobApp import views

urlpatterns = [
    path('',views.index_view),
    path('govtjob_home',views.govtjobs_home_view),
    path('bank_jobs',views.bankjobs_details_view),
    path('filter',views.filter_view),
    path('railwayjobs_details',views.railwayjob_view),
    path('policejobs_details',views.policejob_view),
    path('forestjobs_details',views.forestjob_view)
]

