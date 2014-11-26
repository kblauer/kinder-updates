<h1>Elementary Update</h1>
<h3>A web, android, and iOS app for keeping track of your children while they are at school!</h3>

<h2>Website Appendix / Setup Instructions</h2>

These instructions are here in order to allow you to setup your django installation and development environment on a virtualenv, which essentially isolates a python installation as well as the included packages (django, etc) so that other python installations cannot interfere with this install, and we have a solid base to work on.

NOTE: make sure that once you go through all of these directions, you only interact with the django project from within the virtualenv.  This is explained further down, but just remember: 'workon kinderUpdate'


<h3>----- AMAZON EC2 RUNNING SERVER INSTANCE ----------</h3>

We currently have an amazon ec2 server running the newest version of the site.  

You can access this website by going here: http://ec2-54-68-187-75.us-west-2.compute.amazonaws.com/

Any and all testing is equivalent for this version as well as the django local servers below.  You don't really need to follow these directions, just go to the link above.

In order to login to the site, use the following credentials:

|TEACHER ROLE       | PARENT ROLE       |
|-------------------|-------------------|
|username = teacher | username = parent |
|password = test    | password = test   |


<h3>  WINDOWS INSTRUCTIONS </h3>
<ol>
<li>Uninstall any and all versions of python you currently have installed (sorry :( )</li>
<li>Install Python v2.7 (32-bit) and git
    (make sure to add python to PATH in install options)
    (for git install, choose Use git from Git Bash only, and 
        checkout windows-style, commit unix-style line endings)
</li>

<li>go here: https://pypi.python.org/pypi/setuptools and install setuptools. For windows 7, download ez_setup.py and run in the command line 

```cd Downloads && python ez_setup.py```
</li>
    
<li> ```cd \path-to-python2.7-install\Scripts && easy_install pip```
!! replace path-to-python2.7-install with your install location !!
</li>
        
<li> ```pip install virtualenvwrapper-win``` </li>

<li> ```mkvirtualenv kinderUpdate``` </li>

**** Before continuing, you should have (kinderUpdate) at the beginning of your command line ***
**** if you don't, type ```workon kinderUpdate``` to get out of the virtualenv, type ```deactivate``` ***

<li>```cd \```</li>
<li>```pip install django```</li>
<li>navigate to your desired project parent directory (e.g. C:\dev\) in windows explorer, then right click and press 'Git Bash Here'</li>
<li>in the command line that pops up, enter 
```git clone https://github.com/kblauer/kinder-updates.git```
</li>

<li>To run the local django server, go back to normal windows command line, make sure you are in the correct virtualenv, and 
    ```cd dev-path-here/kinder-updates && python manage.py runserver```
</li>

<li> Navigate to localhost:8000 in browser</li>
</ol>


<h3>LINUX INSTRUCTIONS </h3>

<ol>
<li> Install Python v2.7 via Package manager</li>
<li>install python-setuptools & git (both come from most package managers)</li>
<li> ```sudo easy_install pip```</li>
<li> ```sudo pip install virtualenvwrapper```</li>
<li> add the following to your shell's startup file (.bashrc, .zshrc, etc)

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/directory-you-do-development-in
    source /usr/local/bin/virtualenvwrapper.sh
    
    !! replace directory-you-do-development-in with your directory workspace !!
    
<li> ```mkvirtualenv kinderUpdate```</li>

**** Before continuing, you should have (kinderUpdate) at the beginning of your command line ***
**** if you don't, type ```workon kinderUpdate``` to get out of the virtualenv, type ```deactivate``` ***

<li> ```pip install django```</li>
<li> navigate to your desired project parent directory (e.g. ~/workspace/) </li>
<li> ```git clone https://github.com/kblauer/kinder-updates.git``` </li>

<li>To run the local django server, ```cd kinder-updates && python manage.py runserver``` </li>
<li> Navigate to ```localhost:8000``` in browser </li>
