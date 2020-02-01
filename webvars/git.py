from github import Github

username = 'GreerPage'
g = Github("c771249f357c454a7fecbe345edc2a5a23963cd6")
repos = []
repoURL = []
repoDescription = []
stars = []
size = []
lastPushed = []
for repo in g.get_user().get_repos(visibility='public'):
    if repo.owner.login == username:
        repos.append(repo.name)
        repoURL.append(repo.html_url)
        repoDescription.append(repo.description)
        size.append(str(repo.size))
        stars.append(str(repo.stargazers_count))
        lastPushed.append(str(str(repo.pushed_at).split().pop(0)))
