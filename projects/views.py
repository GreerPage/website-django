from django.shortcuts import render
import threading
from webvars import vars
from django.http import HttpResponse, Http404, JsonResponse
import json
from websiteDjango import settings
from gitapi import secrets
from gitapi import views
from github import Github
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
    repos = get_repos()
    if reponame not in repos:
        raise Http404()
    context = {
        'reponame': reponame,
        'linknum': '1',
        'sociallinks': zip(vars.medialinks, vars.imgnames),
        'bottom': True,
        'repos': repos
    }
    return render(request, 'gitrepo.html', context)

def get_repos():
    g = Github(secrets.token)
    username = views.username
    repos = {}
    for repo in g.get_user().get_repos(visibility='public'):
        if repo.owner.login == username:
            repos[repo.name] = {}
            repos[repo.name]['d'] = repo.description
            repos[repo.name]['url'] = repo.html_url
    return repos

def sam(request):
    return render(request, 'sam.html')
