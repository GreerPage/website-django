from github import Github
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
username = 'GreerPage'
g = Github(open(dir_path + "/gt.txt", "r").read().replace('\n', ''))
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
    

