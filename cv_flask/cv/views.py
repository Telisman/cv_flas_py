from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Info,Education,WorkExperience,Portfolio

def CVHomePage(request):
    info = Info.objects.all()
    education  = Education.objects.all()
    work  = WorkExperience.objects.all()
    portfolio  = Portfolio.objects.all()
    context = {'info': info,
               'education': education,
               'work': work,
               'portfolio': portfolio,
               }

    return render(request, 'cv_page.html',context)
