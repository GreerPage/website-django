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
    if reponame not in git.getInfoForTable():
        raise Http404()
    langs = git.getLanguages(reponame)
    x, one = 0, False
    for key in langs:
        if x == 0: first = key
        if x == len(langs)-1: last = key
        x+=1
    if len(langs) == 1: one, first, last =True, '', ''
    
    context = {
        'reponame': reponame,
        'link': git.getURL(reponame),
        'linknum': '1',
        'readme': git.getREADME(reponame),
        'repos': git.getInfoForTable,
        'sociallinks': zip(vars.medialinks, vars.imgnames),
        'bottom': True,
        'langs' : langs,
        'first':first,
        'last': last,
        'one': one,
    }
    return render(request, 'gitrepo.html', context)

def sam(request):
    return render(request, 'sam.html')