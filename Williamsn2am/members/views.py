from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    myMembers = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'Myembers': myMembers,
    
    }
    return HttpResponse(template.render(context,request))