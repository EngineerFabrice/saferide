
#from django.contrib import admin
#from django.urls import path,include

#urlpatterns = [
 #   path('admin/', admin.site.urls),
#    path('',include("myApp.urls")),
#]

from django.contrib import admin
from django.urls import path
from myApp import views  # Replace myApp with the name of your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Empty path ('') mapped to a view
]

