from django.shortcuts import render
from django.http import JsonResponse
from .secrets import token
from github import Github
import os
import base64
from markdown import markdown
import requests
import json
from websiteDjango import settings
import datetime
from webvars import vars as vars_file

username = requests.get('https://api.github.com/user', headers = {'Authorization': 'token {}'.format(token)}).json()['login']
g = Github(token)

# Create your views here.
def projects_page(request):
    repos = {}
    for repo in g.get_user().get_repos(visibility='public'):
        if repo.owner.login == username:
            repos[repo.name] = {}
            repos[repo.name]['url'] = repo.html_url
            repos[repo.name]['description'] = repo.description
            repos[repo.name]['language'] = repo.language
            repos[repo.name]['languageColor'] = vars_file.repocolors[repo.language]
    
    return JsonResponse(repos)