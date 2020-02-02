from django.shortcuts import render
import threading
from webvars import vars, git

def index(request): 
    context = {
        'medialinks': vars.medialinks,
        'repos': zip(git.repos, git.repoURL, git.repoDescription, git.size, git.stars, git.lastPushed, git.language),
    }
    return render(request, 'projects.html', context)