from django.shortcuts import render
import threading
from webvars import vars, git
from django.http import HttpResponse, Http404, JsonResponse
import json
from websiteDjango import settings
import os

def index(request):    
    context = {
        'linknum': '1',
        'bottom': True,
        'sociallinks': zip(vars.medialinks, vars.imgnames),
        'host': request.get_host()
    }
    return render(request, 'projects.html', context)

def gitpage(request, reponame):
    if reponame not in git.getInfoForTable():
        raise Http404()
    context = {
        'reponame': reponame,
        'linknum': '1',
        'repos': git.getGitInfo('getInfoForTable', "")[0],
        'sociallinks': zip(vars.medialinks, vars.imgnames),
        'bottom': True,
    }
    return render(request, 'gitrepo.html', context)

def sam(request):
    return render(request, 'sam.html')

def update(request):
    git.updateAll()
    with open(os.path.join(settings.BASE_DIR, 'json/git.json'), 'r') as e:
        data = json.load(e)
    return JsonResponse(data, json_dumps_params={'indent': 2})