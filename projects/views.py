from django.shortcuts import render
import threading
from webvars import vars, git
from django.http import HttpResponse, Http404

def index(request): 
    context = {
        'repos': git.getInfoForTable,
        'colors': vars.repocolors,
        'linknum': '1',
        'bottom': True,
        'sociallinks': zip(vars.medialinks, vars.imgnames),
    }
    return render(request, 'projects.html', context)
def gitpage(request, reponame):
    if reponame not in git.getInfoForTable('repos'):
        raise Http404()
    context = {
        'reponame': reponame,
        'link': git.getURL(reponame),
        'linknum': '1',
        'readme': git.getREADME(reponame),
        'repos': git.getInfoForTable,
        'sociallinks': zip(vars.medialinks, vars.imgnames),
        'bottom': True,
    }
    return render(request, 'gitrepo.html', context)

def sam(request):
    return render(request, 'sam.html')