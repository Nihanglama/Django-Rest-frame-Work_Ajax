from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('My_note.urls')),
    path('',include('frontend.urls')),

]
