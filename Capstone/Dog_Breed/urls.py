"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]"""
from django.urls import path

from. import views

urlpatterns = [
   
    path('', views.home, name = 'home'),
    #path('prompt', views.prompt, name = 'prompt'),
    
      
]
