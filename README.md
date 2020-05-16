# personal website

Repository for my [website](https://greerpage.com)

## starting off

- Cd to root directory and run `pip3 install -r requirements.txt`
- In `websiteDjango/settings.py` change `Debug = False` to `Debug = True` so that django will serve static files.
- Make the file `gitapi/secrets.py` in this file write: `token = <your token>` find out more about github auth tokens [here](https://github.com/settings/tokens)
- Cd to the root directory and run ```python3 manage.py runserver``` this will start the server on [http://localhost:8000](http://localhost:8000)
- If you recieved an error this might be due to some sort of error with `gitapi/secrets.py`
- After these changes the server should start up. Although, it will display your github repository info on the projects page
## front end
- The front end of this site is done [reactjs](https://reactjs.org) and just plain html.
- [Django](https://www.djangoproject.com/) handles the routing and rendering of templates.
- React is used to fetch information from the api endpoints (`api/projects/`). Once it does so, it renders the inforamtion that you see in the project pages.

## back end
- The backend of this site was done in [Django](https://www.djangoproject.com/).
- When using the "api" django is communicating with the GitHub API via the python wrapper [PyGitHub](https://github.com/PyGithub/PyGithub).
- When it gets a response, it will return the information need for react to render the page.
```javascript
// basic example of how react and django communicate
fetch('api/projects/website-django')
    .then(res => res.json())
    .then(data => {
        this.setState({data: data});
    });
```
## directories
- about — about page
- homepage — home page
- projects — project page
- static — contains css, js, and images
- templates — all HTML files
- websiteDjango — main configuration files like routing and settings
- gitapi — contains code for the api endpoints