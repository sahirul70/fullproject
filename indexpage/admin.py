from django.contrib import admin
from .models import Contact, Team, Project,Testimonial, Service, Patners, Awards,Appointment,Services,ProjectAbout,Post,Commant
# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    list_display = ['title', 'image']
    search_fields = ['title']
admin.site.register(Team, TeamAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_field = ['title']

admin.site.register(Project,ProjectAdmin)



class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_field = ['title']

admin.site.register(Testimonial,TestimonialAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_field = ['title']

admin.site.register(Service,ServiceAdmin)

class PatnersAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(Patners,PatnersAdmin)

class AwardsAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_field = ['title']

admin.site.register(Awards,AwardsAdmin)

class AppiontmentAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject']
    search_field =['subject']
admin.site.register(Appointment,AppiontmentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','massage']
    search_field =['subject']
admin.site.register(Contact,ContactAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title','description','image']
admin.site.register(Services,ServiceAdmin)

class ProjectAboutAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_field = ['title']

admin.site.register(ProjectAbout,ProjectAboutAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','body']
    search_field =['title']
admin.site.register(Post,PostAdmin)

class CommantAdmin(admin.ModelAdmin):
    list_display = ['name','email']
admin.site.register(Commant,CommantAdmin)
