from django.shortcuts import render
import threading
from webvars import vars, git
from django.http import HttpResponse, Http404

def index(request): 
    context = {
        'medialinks': vars.medialinks,
        'repos': zip(git.repos, git.repoURL, git.repoDescription, git.size, git.stars, git.lastPushed, git.language),
    }
    return render(request, 'projects.html', context)
def gitpage(request, reponame):
    if reponame not in git.repos:
        raise Http404()
    return HttpResponse('This is the %s page' % reponame)