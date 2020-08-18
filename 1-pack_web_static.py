#!/usr/bin/python3
"""Generate .tgz archive from the contents of the web_static"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress files"""
    try:
        local("mkdir -p versions")
        now = datetime.now()
        current_date = now.strftime("%Y%m%d%H%M%S")
        f_path = "versions/web_static_" + current_date
        local("tar -cvzf {}.tgz web_static"
              .format(f_path))
        return f_path
    except:
        return None
