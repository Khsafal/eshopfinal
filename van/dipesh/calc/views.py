from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import file

def view_upload(request):
    return render(request,'upload.html')

def view_upload_pic(request):
  
    img = request.FILES['file']
    Bookfile = file(file = img)
    Bookfile.save()
    return HttpResponse("uploaded..")