from github import Github
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
username = 'GreerPage'
token = open(dir_path + "/gt.txt", "r")
#g = Github('58439d586c37d36ebf1e645a30d1e8ba15229951')
t = token.read().replace('\n', '')
print(t)
g = Github(t)
token.close()
repos = []
repoURL = []
repoDescription = []
stars = []
size = []
lastPushed = []
language = []
for repo in g.get_user().get_repos(visibility='public'):
    if repo.owner.login == username:
        repos.append(repo.name)
        repoURL.append(repo.html_url)
        repoDescription.append(repo.description)
        size.append(str(repo.size))
        stars.append(str(repo.stargazers_count))
        lastPushed.append(str(str(repo.pushed_at).split().pop(0)))
        language.append(repo.language)
