from github import Github
import os
import base64
from markdown import markdown
import requests
import json
from websiteDjango import settings
import datetime
try: from .vars import repocolors
except ImportError: from vars import repocolors

dir_path = os.path.dirname(os.path.realpath(__file__))
username = 'GreerPage'
token = open(dir_path + "/gt.txt", "r").read().replace('\n', '')
g = Github(token)

def getInfoForTable(reponame = ''):
    repos = {}
    for repo in g.get_user().get_repos(visibility='public'):
        if repo.owner.login == username:
            repos[repo.name] = []
            repos[repo.name].append(repo.html_url)
            repos[repo.name].append(repo.description)
            repos[repo.name].append(repo.language)
            repos[repo.name].append(repocolors[repo.language])
    if reponame == '':
        return repos 
    else:
        return repos[reponame]

def getREADME(reponame):
    try:
        user = g.get_user()
        repo = user.get_repo(reponame)
        readme = repo.get_contents('README.md')
        readme = (base64.b64decode(readme.content).decode('Utf-8'))
        return markdown(readme)
    except:
        return 'ERROR: Cannot find README.md in this repository :('

def getURL(reponame):
    user = g.get_user()
    repo = user.get_repo(reponame)
    url = repo.html_url
    return url

def getLanguages(rep):
    total = 0
    user = g.get_user()
    repo = user.get_repo(rep)
    langs = requests.get(repo.languages_url, headers = {'Authorization': 'token {}'.format(token)}).json()
    for key in langs:
        total += langs[key]
    for key in langs:
        per = round(langs[key]/total*100, 2)
        langs[key] = [per, repocolors[key]]
    return langs

def getGitInfo(name, arg = ''):
    if 'json' not in os.listdir(settings.BASE_DIR):
        os.mkdir(os.path.join(settings.BASE_DIR, 'json'))
    if 'git.json' not in os.listdir(os.path.join(settings.BASE_DIR, 'json')):
        open(os.path.join(settings.BASE_DIR, 'json', 'git.json'), 'w+')
    file, e, for_json = os.path.join(settings.BASE_DIR, 'json', 'git.json'), datetime.datetime.now(), {}
    content = open(file, 'r').read()
    current_time = e.strftime('%H %M')
    current_time = current_time.split()
    for i in range(len(current_time)): current_time[i] = int(current_time[i])
    if content == '':  
        func = globals()[name](arg)
        for_json['{}({})'.format(name, arg)] = [func, {'time': current_time}]
        with open(file, 'w') as json_file:
            json.dump(for_json, json_file)
        return for_json['{}({})'.format(name, arg)]
    else:
        with open(file) as f:
            content = json.load(f)
        if '{}({})'.format(name, arg) not in content:
            func = globals()[name](arg)
            content['{}({})'.format(name, arg)] = [func, {'time': current_time}]
            with open(file, 'w') as json_file:
                json.dump(content, json_file)
            return content['{}({})'.format(name, arg)]
        else:
            info = content['{}({})'.format(name, arg)]
            if current_time[0] - info[1]['time'][0] > 0 or current_time[1] - info[1]['time'][1] >= 10:
                func = globals()[name](arg)
                content['{}({})'.format(name, arg)] = [func, {'time': current_time}]
                with open(file, 'w') as json_file:
                    json.dump(content, json_file)
                return content['{}({})'.format(name, arg)]

            else: return info

def updateAll():
    repos = []
    for repo in g.get_user().get_repos(visibility='public'):
        if repo.owner.login == username:
            repos.append(repo.name)
    getGitInfo('getInfoForTable', '')
    for repo in repos:     
        getGitInfo('getREADME', repo)
        getGitInfo('getURL', repo)
        getGitInfo('getLanguages', repo)
    
    return 'success'