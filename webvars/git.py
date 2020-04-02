from github import Github
import os
import base64
from markdown import markdown
import requests
from .vars import repocolors

dir_path = os.path.dirname(os.path.realpath(__file__))
username = 'GreerPage'
token = open(dir_path + "/gt.txt", "r").read().replace('\n', '')
g = Github(token)

def getInfoForTable(list1=''):
    repos, repoURL, repoDescription, language, colors = [], [], [], [], []
    for repo in g.get_user().get_repos(visibility='public'):
        if repo.owner.login == username:
            repos.append(repo.name)
            repoURL.append(repo.html_url)
            repoDescription.append(repo.description)
            language.append(repo.language)
            colors.append(repocolors[repo.language])
    if list1 == '':
        return zip(repos, repoURL, repoDescription, language, colors)
    else:
        return vars()[list1]

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

def getLanguages(rep=''):
    if rep != '':
        total = 0
        user = g.get_user()
        repo = user.get_repo(rep)
        print(repo.languages_url)
        langs = requests.get(repo.languages_url, headers = {'Authorization': 'token {}'.format(token)}).json()
        for key in langs:
            total += langs[key]
        for key in langs:
            per = round(langs[key]/total*100, 2)
            langs[key] = [per, repocolors[key]]
        return langs
    languages, total = {}, 0
    for repo in g.get_user().get_repos(visibility='public'):
        if repo.owner.login == username:
            langs = requests.get(repo.languages_url, headers = {'Authorization': 'token {}'.format(token)}).json()
            languages[repo.name] = {}
            for key in langs:
                languages[repo.name][key] = [langs[key]] 
    
    for key in languages:
        for k in languages[key]:
            e = languages[key][k][0]
            total += e
        for i in languages[key]:
            e = languages[key][i][0]
            languages[key][i][0] = round(e/total*100, 2)
            languages[key][i].append(repocolors[i])
        
    return languages


