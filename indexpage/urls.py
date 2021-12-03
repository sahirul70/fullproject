from django.urls import path
from .import views

app_name = 'indexpage'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_form/',views.contact, name='contact_form'),
    path('it-slutions/',views.itsolutions, name='it-solution'),
    path('about/',views.about, name='about'),
    path('team/',views.team, name='team'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    #path('single/<int:id>',views.post_detail, name='single'),
    path('<int:id>/', views.postget, name='postget'),
]