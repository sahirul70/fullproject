from django.shortcuts import render
from .models import Team, Project, Testimonial, Service, Patners, Awards
from .forms import AppoinmentForms
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    team_data = Team.objects.all()
    project_data = Project.objects.all()
    testimonial_data = Testimonial.objects.all()
    service_data = Service.objects.all()
    patners_data = Patners.objects.all()
    award_data = Awards.objects.all()
    
    
    if request.method=='POST':
        appointment_form = AppoinmentForms(request.POST)
        
        if appointment_form.is_valid():
            appointment_form.save()
             #redirect to a new URL:
        return HttpResponseRedirect(request.path_info)
    else:
        
        appointment_form = AppoinmentForms()

    context={
        'team_data':team_data,
        'project_data': project_data,
        'testimonial_data':testimonial_data,
        'service_data': service_data,
        'patners_data':patners_data,
        'award_data':award_data,
    }

    return render(request,'index.html',context)