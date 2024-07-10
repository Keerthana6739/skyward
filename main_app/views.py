from django.shortcuts import render,redirect
from main_app.views import *
import json
from .forms import *
from django.contrib import messages
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import base64
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse #This is i am using in client contact edit for redirect to main page

from django.utils import timezone


# Create your views here.

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'Administration/dashboard.html')

def users(request):
    return render(request, 'Administration/users.html')

def ref(request):
    form=ReftemplateForm()
    return render(request, 'Administration/ref.html',{'form':form})
def refcreate(request):
    form=ReftemplateForm()
    return render(request, 'Administration/refcreate.html',{'form':form})

def refedit(request):
    form=ReftemplateForm()
    return render(request, 'Administration/refedit.html',{'form':form})

def reft(request):
    form=ReftlangmasterForm()
    return render(request, 'Administration/reft.html',{'form':form})

def tc(request):
    form=TermsAndConditionsForm()
    return render(request, 'Administration/tc.html',{'form':form})

def manifest(request):
    form=ManifestTemplateForm()
    return render(request, 'Administration/manifest.html',{'form':form})

def manifestcreate(request):
    form = ManifestTemplateForm()
    form1 = PrintOutDetailsManifestForm()
    form2 = PrintOutBottomManifestForm()
    combined_forms = {
        'form': form,
        'printout': form1,
        'printbottom': form2,
    }
    return render(request, 'Administration/manifestcreate.html', combined_forms)

def manifestedit(request):
    form = ManifestTemplateForm()
    form1 = PrintOutDetailsManifestForm()
    form2 = PrintOutBottomManifestForm()
    combined_forms = {
        'form': form,
        'printout': form1,
        'printbottom': form2,
    }
    return render(request, 'Administration/manifestedit.html', combined_forms)

def sms(request):
    form=SmstemplateForm()
    return render(request, 'Administration/sms.html',{'form':form})
def usergroup(request):
    form=UsergroupmasterForm()
    return render(request, 'Administration/usergroup.html',{'form':form})

def booking(request):
    form=BookingpurposeForm()
    return render(request, 'Administration/booking.html',{'form':form})

def service(request):
    form=ServicessuppliersForm()
    return render(request, 'Administration/service.html',{'form':form})

def servicetypes(request):
    form=ServicestypesForm()
    return render(request, 'Administration/servicetypes.html',{'form':form})

def reports(request):
    form= ReportsupermissionsForm()
    return render(request, 'Administration/reports.html',{'form':form})
def reftwords(request):
 
    form=Reftwords()
    return render(request, 'Administration/reftwords.html',{'form':form})

def scheduled(request):
    form= ScheduledreportsForm()
    return render(request, 'Administration/scheduled.html',{'form':form})

def station(request):
    form= StationvatForm()
    return render(request, 'Administration/station.html',{'form':form})

def users(request):
    return render(request, 'Administration/users.html')

def createuser(request):
    return render(request, 'Administration/createuser.html')
def edituser(request):
    return render(request, 'Administration/editreuser.html')

def permission(request):
    return render(request, 'Administration/permission.html')

def toperationcreae(request):
    form=AircraftTypeForm()
    return render(request, 'OperationAdmin/operationcreate.html',{'form':form})

def serviceload(request):
    form=ServiceLoadForm()
    return render(request, 'OperationAdmin/serviceload.html',{'form':form})

def aircraft(request):
    form=AirCraftForm()
    return render(request, 'OperationAdmin/aircraft.html',{'form':form})

def savedroutes(request):
    form=SaveRouteForm()
    return render(request, 'OperationAdmin/savedroutes.html',{'form':form})

def dstnotifications(request):
    form=DSTNotificationsForm()
    return render(request, 'OperationAdmin/dstnotifications.html',{'form':form})

def dstrestrict(request):
    form=DSTRestrictForm()
    return render(request, 'OperationAdmin/dstrestrict.html',{'form':form})

def dsttimeaddon(request):
    form=DSTTimeAddonForm()
    return render(request, 'OperationAdmin/dsttimeaddon.html',{'form':form})

def acavailability(request):
    form=AcAvailabilityForm()
    return render(request, 'OperationAdmin/acavailability.html',{'form':form})

def acavailabilitytype(request):
    form=AcAvailabilityTypeForm()
    return render(request, 'OperationAdmin/acavailabilitytype.html',{'form':form})

def ssr(request):
    form=SpecialServicesForm()
    return render(request, 'OperationAdmin/ssr.html',{'form':form})

def queues(request):
    form=QueuesForm()
    return render(request, 'OperationAdmin/queues.html',{'form':form})

def destination(request):
    form=DestinationForm()
    return render(request, 'OperationAdmin/destination.html',{'form':form})

def createpage(request):
    form=DestinationForm()
    return render(request, 'OperationAdmin/createpage.html',{'form':form})

def edit(request):
    form=DestinationForm()
    return render(request, 'OperationAdmin/edit.html',{'form':form})
