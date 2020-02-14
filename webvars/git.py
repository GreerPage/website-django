from github import Github
import os
import base64

dir_path = os.path.dirname(os.path.realpath(__file__))
username = 'GreerPage'
g = Github(open(dir_path + "/gt.txt", "r").read().replace('\n', ''))

def getInfoForTable(list1=''):
    repos, repoURL, repoDescription, stars, size, lastPushed,language = [], [], [], [], [], [], []
    for repo in g.get_user().get_repos(visibility='public'):
        if repo.owner.login == username:
            repos.append(repo.name)
            repoURL.append(repo.html_url)
            repoDescription.append(repo.description)
            size.append(str(repo.size))
            stars.append(str(repo.stargazers_count))
            lastPushed.append(str(str(repo.pushed_at).split().pop(0)))
            language.append(repo.language)
    if list1 == '':
        return zip(repos, repoURL, repoDescription, size, stars, lastPushed,language)
    else:
        return vars()[list1]

def getREADME(reponame):
    try:
        user = g.get_user()
        repo = user.get_repo(reponame)
        readme = repo.get_contents('README.md')
        readme = (base64.b64decode(readme.content).decode('Utf-8'))
        return readme
    except:
        return 'ERROR: Cannot find README.md in this repository :('  

def getURL(reponame):
    user = g.get_user()
    repo = user.get_repo(reponame)
    url = repo.html_url
    return url

