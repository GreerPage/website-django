from django.shortcuts import render
from webvars import vars

# Create your views here.
def index(request):
    context = {
        'medialinks': vars.medialinks,
        'linknum': '',
        'links': zip(vars.medialinks, vars.imgnames),
    }
    return render(request, 'home.html', context)
    