#!/usr/bin/python3
"""Full deployment"""
from fabric.api import *
import os.path
import re
from datetime import datetime


env.hosts = ['34.73.35.13', '3.88.220.170']
env.user = 'ubuntu'


def do_pack():
    """Compress files"""

    try:
        local("mkdir -p versions")
        now = datetime.now()
        current_date = now.strftime("%Y%m%d%H%M%S")
        f_path = "versions/web_static_" + current_date + ".tgz"
        local("tar -cvzf {} web_static"
              .format(f_path))
        return f_path
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive"""
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, "/tmp/")
        file_name = re.search('versions/(.*).tgz',
                              archive_path)
        run("mkdir -p /data/web_static/releases/{}/"
            .format(file_name.group(1)))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name.group(1), file_name.group(1)))
        run("rm /tmp/{}.tgz".format(file_name.group(1)))
        run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/"
            .format(file_name.group(1), file_name.group(1)))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(file_name.group(1)))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name.group(1)))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive"""
    f_path = do_pack()
    if f_path is None:
        return False
    r = do_deploy(f_path)
    return r
