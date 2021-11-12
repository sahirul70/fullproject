from django.db import models
#from django.db.models.fields import CharField
from django.db.models.fields import BLANK_CHOICE_DASH


# Create your models

class Team(models.Model):

    title = models.CharField(max_length=50)
    short_description = models.TextField()

    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.title



class Project(models.Model):
    title = models.CharField(max_length= 30)
    short_name =  models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='project/')

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length= 30)
    short_name =  models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='testimonial/')

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length= 30)
    description = models.TextField()
    image = models.ImageField(upload_to='service/')

    def __str__(self):
        return self.title

class Patners(models.Model):

    image = models.ImageField(upload_to='patmers/')
    image_hover = models.ImageField(upload_to='patmers/')

class Awards(models.Model):
    title = models.CharField(max_length= 30)
    description = models.TextField()
    image = models.ImageField(upload_to='awards/')

    def __str__(self):
        return self.title

class Appoinment(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name