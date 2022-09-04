from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def CVHomePage(request):
    return render(request, 'cv_page.html')
