# Django Website

Repository for my [website](https://greerpage.com)

## Starting Off

- Cd to root directory and run `pip3 install -r requirements.txt`
- In `websiteDjango/settings.py` change ```Debug = False``` to ```Debug = True```
- Make the file `gitapi/secrets.py` in this file write: `token = <your token>` find out more about github auth tokens [here](https://github.com/settings/tokens)
- Cd to the root directory and run ```python3 manage.py runserver``` this will start the server on [http://localhost:8000](http://localhost:8000)
- If you recieved an error this might be due to some sort of error with `gitapi/secrets.py`
- After these changes the server should start up. Although, it will display your github repository info on the projects page

## GitHub Information
- I am communicating with the [Github Api](https://developer.github.com/v3/) to get the information seen on the projects pages.
- To do this I am using a python wrapper api called [PyGitHub](https://github.com/PyGithub/PyGithub)

## react
- I am using a minimal amount of [reactjs](https://reactjs.org) in the front end to handle fetching the git information
- This code can be found in `static/js`
- I originaly had all of the git info being fetched in the backend on page render, this drastically slowed down the load times of the site, so I decided to make the requests in the front end.
- I wrote all of the react in pure js rather than in JSX for reasons that I cannot explain.
- If you don't know how to use react in pure js, check out an online compiler [here](https://babeljs.io/repl)
- Rather than fetching to the full github api I set up my own api that has only the information I need, this is what the react interacts with

## HTML
- All HTML files can be found in `/templates`
- These files are technically in the django template language so it is not pure HTML
- "head.html" contains all of the constant data throughout all files (head, fonts, nav bar, etc)
- All other HTML files extend `head.html`

## Python

- The backend python framework I am using is called [Django](https://www.djangoproject.com/)
- It has a fairly complex file structure that you can read more about [here](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
- Django has lots of features that are meant for large scale applications not like this one and it is kind of overkill for my site
- This is why I might be changing to [Flask](https://flask.palletsprojects.com/en/1.1.x/) in the future

## Api
- The "api" is very simple, all it does is make a request to the github api when it is requested and returns only the necessary information. 
- This is what the react fetchs from


## Directories
- about — about page
- homepage — home page
- projects — base project page
- static — contains css, js, and images
- templates — all HTML files
- websiteDjango — main configuration files like routing and settings
- gitapi — contains code for the api endpoints
```
test
does
this
work???
```