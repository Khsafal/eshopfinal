from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('uploadfile/',view_upload),
    path('uploadfile/upload',view_upload_pic),


]