<h1>Django Website</h1>

<p>Repository for my <a href="https://greerpage.com">website</a></p>

<h2>Starting Off</h2>
<ul>
    <li>Cd to root directory and run "pip3 install -r requirements.txt"</li>
    <li>In "websiteDjango/settings.py" change Debug=False to Debug=True</li>
    <li>Make the file "/webvars/gt.txt" in it put a <a href="https://github.com/settings/tokens">GitHub Auth Token</a></li>
    <li>You may also want to change the username value in /webvars/git.py to your GitHub username</li>
    <li>Cd to the root directory and run "python3 manage.py runserver" this will start the server on  <a href="http://localhost:8000">http://localhost:8000</a></li>
    <li>If you recieved an error this might be due to some sort of error with /webvars/gt.txt</li>
    <li>After these changes the server should start it. Although, it will display your github repository info on the projects page</li>
</ul>

<h2>Projects Page</h2>
<ul>
    <li>In order to pull the information for the projects page I am using the python library <a href="https://github.com/PyGithub/PyGithub">PyGitHub</a></li>
    <li>/webvars/git.py collects all of the necessary information from GitHub</li>
</ul>

<h2>HTML</h2>
<ul>
    <li>All HTML files can be found in /templates</li>
    <li>These files are technically in the django template language so it is not pure HTML</li>
    <li>"head.html" contains all of the constant data throughout all files (head, fonts, nav bar, etc)</li>
    <li>All other HTML files extend "head.html"</li>
</ul>

<h2>Directories</h2>
<ul>
    <li>about — about page</li>
    <li>env — python virtualenv</li>
    <li>homepage — home page</li>
    <li>projects — project page</li>
    <li>static — contains css, js, and images</li>
    <li>templates — all HTML files</li>
    <li>websiteDjango — main configuration files</li>
    <li>webvars — contains backend python</li>
</ul>
