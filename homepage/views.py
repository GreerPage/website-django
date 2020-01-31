from django.shortcuts import render
from webvars import vars

# Create your views here.
def index(request):
    context = {
        'medialinks': vars.medialinks,
    }
    return render(request, 'home.html', context)
    