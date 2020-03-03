# Django Website

Repository for my [website](https://greerpage.com)

## Starting Off

- Cd to root directory and run `pip3 install -r requirements.txt`
- In "websiteDjango/settings.py" change ```Debug = False``` to ```Debug = True```
- Make the file "/webvars/gt.txt" in it put a [GitHub Auth Token](https://github.com/settings/tokens)
- You may also want to change the username value in /webvars/git.py to your GitHub username
- Cd to the root directory and run ```python3 manage.py runserver``` this will start the server on [http://localhost:8000](http://localhost:8000)
- If you recieved an error this might be due to some sort of error with /webvars/gt.txt
- After these changes the server should start up. Although, it will display your github repository info on the projects page

## Projects Page
- In order to pull the information for the projects page I am using the python library [PyGitHub](https://github.com/PyGithub/PyGithub)
- /webvars/git.py collects all of the necessary information from GitHub


## HTML
- All HTML files can be found in /templates</li>
- These files are technically in the django template language so it is not pure HTML
- "head.html" contains all of the constant data throughout all files (head, fonts, nav bar, etc)
- All other HTML files extend "head.html"

## Python

- Most of the python that handles variables etc can be found in /webvars
- /webvars/git.py handles all of the GitHub data
- /webvars/vars.py stores many of the longer variables that get imported into templates


## Directories
- about — about page</li>
- env — python virtualenv</li>
- homepage — home page</li>
- projects — project page</li>
- static — contains css, js, and images
- templates — all HTML files
- websiteDjango — main configuration files
- webvars — contains backend python
