from django.shortcuts import render
import threading
from webvars import vars, git
from django.http import HttpResponse, Http404

def index(request): 
    context = {
        'medialinks': vars.medialinks,
        'repos': zip(git.repos, git.repoURL, git.repoDescription, git.size, git.stars, git.lastPushed, git.language),
        'linknum': '1',
    }
    return render(request, 'projects.html', context)
def gitpage(request, reponame):
    if reponame not in git.repos:
        raise Http404()
    return HttpResponse(f"<title>{reponame}</title> <p style='position: absolute; top: 50%; left: 50%; transform: translatex(-50%)'>You have reached the {reponame} page :)")