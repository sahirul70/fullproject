from django.shortcuts import render,get_object_or_404, redirect
from .models import Contact, Team, Project, Testimonial, Service, Patners, Awards, Services,ProjectAbout,Post
from .forms import AppointmentForm, ContactForm, CommantForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    team_data = Team.objects.all()
    project_data = Project.objects.all()
    testimonial_data = Testimonial.objects.all()
    service_data = Service.objects.all()
    patners_data = Patners.objects.all()
    award_data = Awards.objects.all()

    if request.method == 'POST':

        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        appointment_form = AppointmentForm()
    
    context={
        'team_data':team_data,
        'project_data': project_data,
        'testimonial_data':testimonial_data,
        'service_data': service_data,
        'patners_data':patners_data,
        'award_data':award_data,
    }
    return render(request,'index.html',context)

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect('/')
    else:
        contact_form =ContactForm()
    context ={

    }
    return render(request,'index.html',context)

def itsolutions(request):
    data_service = Services.objects.all()
    context = {
        'data_service': data_service
    }
    return render(request,'it-solution.html',context)

def about(request):

    testimonial_data = Testimonial.objects.all()
    projectabour_data = ProjectAbout.objects.all()
    context = {
        'testimonial_data':testimonial_data,
        'projectabour_data':projectabour_data,
    }
    return render(request,'about.html',context)

def team(request):
    team_data = Team.objects.all()
    context = {
        'team_data':team_data,
    }
    return render(request,'team.html',context)

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        contact_form =ContactForm()
    
    context = {
        
    }
    return render(request,'contact.html',context)
def blog(request):
    bolg_data = Post.objects.all()
    context = {
       'bolg_data':bolg_data,
    }
    return render(request,'blog.html',context)

def postget(request, id):
    post = get_object_or_404(Post,pk = id)
    if request.method == 'POST':
        form = CommantForm(request.POST)
        if form.is_valid():
            commant = form.save(commit = False)
            commant.post = post
            commant.save()
            return redirect('indexpage:postget', id=post.id)
    else:
        form = CommantForm()
    context={
       'post' :post,
        'form' :form,
       
    }
    return render(request,'blogdetails.html',context)