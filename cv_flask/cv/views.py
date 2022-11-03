import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Info,Education,WorkExperience,Portfolio
from django.http import JsonResponse

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

# def api_home(request, *args , **kwargs):
#     print(request.POST)
#     print(request.GET)
#     body = request.body
#     data = {
#
#     }
#     try:
#         data = json.load(body)
#     except:
#         pass
#     # json.dump(dict(request.headers))
#     # data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)
