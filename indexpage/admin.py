from django.contrib import admin
from .models import Team, Project,Testimonial, Service, Patners, Awards,Appoinment
# Register your models here.

class TeamlAdmin(admin.ModelAdmin):

    list_display = ['title', 'image']
    search_fields = ['title']

admin.site.register(Team, TeamlAdmin)


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

class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ['name','email','department']

admin.site.register(Appoinment,AppoinmentAdmin)