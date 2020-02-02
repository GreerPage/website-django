from github import Github

username = 'GreerPage'
g = Github("af1ba77d3384dcd29d9bc5b8b63e4f4cd72b2ff2")
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
