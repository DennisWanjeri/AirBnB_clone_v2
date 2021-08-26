#!/usr/bin/python3
# fabfile that creates an archive and distributes it to a webserver
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

