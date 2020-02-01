from django.shortcuts import render
from webvars import vars, git

# Create your views here.
def index(request):
    context = {
        'medialinks': vars.medialinks,
        'repos': zip(git.repos, git.repoURL, git.repoDescription, git.size, git.stars, git.lastPushed),
        
    }
    return render(request, 'projects.html', context)