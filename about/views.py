from django.shortcuts import render
from webvars import vars

# Create your views here.
def index(request):
    context = {
        'medialinks': vars.medialinks,
        'abouttext': vars.abouttext,
        'linknum': '1',
        'bottom': True,
        'sociallinks': zip(vars.medialinks, vars.imgnames),
        'pc': zip(vars.pclinks, vars.pcparts),
    }
    return render(request, 'about.html', context)