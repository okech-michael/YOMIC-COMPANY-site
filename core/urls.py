from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),  
    path('company/', views.company, name='company'),
    path('pricing/', views.pricing, name='pricing'),
    path('solutions/', views.solutions, name='solutions'),
    path('contact/', views.contact, name='contact'),
    
    
    
    
    
    
    
    ]