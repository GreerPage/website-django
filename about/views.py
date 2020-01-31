from django.shortcuts import render
from webvars import vars

# Create your views here.
def index(request):
    context = {
        'links': vars.pclinks,
        'medialinks': vars.medialinks,
        'abouttext': vars.abouttext,
    }
    return render(request, 'about/about.html', context)