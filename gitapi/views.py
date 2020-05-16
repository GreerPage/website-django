from django.http import JsonResponse
from .secrets import token
from github import Github
import os
import base64
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

def git_pages(request, reponame):
    user = g.get_user()
    repo = user.get_repo(reponame)
    return JsonResponse({reponame: {
                            'url': repo.html_url, 
                            'languages': getLanguages(repo),
                            'readme': getREADME(repo)
                            }
                        })
    
def getREADME(repo):
    try:
        readme = repo.get_contents('README.md')
        readme = (base64.b64decode(readme.content).decode('Utf-8'))
        return readme
    except:
        return 'ERROR: Cannot find README.md in this repository :('

def getLanguages(repo):
    total = 0
    langs = requests.get(repo.languages_url, headers = {'Authorization': 'token {}'.format(token)}).json()
    for key in langs:
        total += langs[key]
    for key in langs:
        per = round(langs[key]/total*100, 2)
        langs[key] = {'percent': per, 'color': vars_file.repocolors[key]}
    return langs