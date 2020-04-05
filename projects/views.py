from django.shortcuts import render
import threading
from webvars import vars, git
from django.http import HttpResponse, Http404, JsonResponse
import json
from websiteDjango import settings
import os

def index(request):    
    context = {
        'repos': git.getGitInfo('getInfoForTable', "")[0],
        'linknum': '1',
        'bottom': True,
        'sociallinks': zip(vars.medialinks, vars.imgnames),
    }
    return render(request, 'projects.html', context)

def gitpage(request, reponame):
    if reponame not in git.getInfoForTable():
        raise Http404()
    langs = git.getGitInfo('getLanguages', reponame)[0]
    x, one = 0, False
    for key in langs:
        if x == 0: first = key
        elif x == len(langs)-1: last = key
        x+=1
    if len(langs) == 1: one, first, last =True, '', ''
    
    context = {
        'reponame': reponame,
        'link': git.getGitInfo('getURL', reponame)[0],
        'linknum': '1',
        'readme': git.getGitInfo('getREADME', reponame)[0],
        'repos': git.getGitInfo('getInfoForTable', "")[0],
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

def update(request):
    git.updateAll()
    with open(os.path.join(settings.BASE_DIR, 'json/git.json'), 'r') as e:
        data = json.load(e)
    return JsonResponse(data, json_dumps_params={'indent': 2})