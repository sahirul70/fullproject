from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields import BLANK_CHOICE_DASH
from django.contrib.auth.models import User


# Create your models

class Team(models.Model):

    title = models.CharField(max_length=50)
    short_description = models.TextField()
    image = models.ImageField(upload_to='team/')
    facebook_link = models.URLField(max_length=100, blank= True)
    github_link = models.URLField(max_length=100,blank= True)
    linkdin_link = models.URLField(max_length=100,blank= True)
    instagram_link = models.URLField(max_length=100,blank= True)

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

class Appointment(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Contact(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    massage = models.TextField()

    def __str__(self):
        return self.name

class Services(models.Model):
    title = models.CharField(max_length=70)
    description =models.TextField()
    image = models.ImageField(upload_to ='service/')

    def __str__(self):
        return self.title
class ProjectAbout(models.Model):
    title = models.CharField(max_length= 30)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='blog/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title
    def get_absolute_url(self):
        return reverse("indexpage:postget", args=[self.pk])

class Commant(models.Model):
    post = models.ForeignKey(Post, related_name='commant',on_delete=CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

