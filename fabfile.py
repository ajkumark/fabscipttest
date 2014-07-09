from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['localhost']

def test():
    with settings(warn_only=True):
        result = local('./manage.py test testapp', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def commit():
    local("git add . && git commit")

def push():
    local("git push")

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
    code_dir = '/home/user/ajai/testproject'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone https://github.com/ajkumark/fabscipttest.git %s" % code_dir)
    with cd(code_dir):
        run("git pull origin master")
        run("touch testapp.wsgi")
