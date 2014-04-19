# coding=utf-8

import time
import json
from datetime import datetime, timedelta
import sys
import os
import socket
import urllib2
import platform

import cherrypy
import htpc
import logging


logger = logging.getLogger('modules.services')

class Services:
    def __init__(self):
        self.logger = logging.getLogger('modules.stats')
    
    
    @cherrypy.expose()
    def index(self):
        return htpc.LOOKUP.get_template('services.html').render(scriptname='services')

    @cherrypy.expose()
    def rebootserver(self):
        self.logger.info("CALLED REBOOT SERVER")
        if sys.platform == 'win32':
            if os.environ.get('OS','') == 'Windows_NT':
                os.system("shutdown -t 0 -r")
        else:
            os.system("reboot")
    
    @cherrypy.expose()
    def outputwatchedplex(self):
        import subprocess
        temp = subprocess.check_output("python /opt/autodelete.py -i 192.168.0.53 -s 2", shell=True)
        output = temp.replace("\n", "<br />")
        return output
    
    @cherrypy.expose()
    def deletewatchedplex(self, *args):
        #must be S, D IN THAT ORDER
        S = args[0]
        D = args[1]
        import subprocess
        temp = subprocess.check_output("python /opt/autodelete.py -i 192.168.0.53 -d " + D + " -s " + S, shell=True)
        output = temp.replace("\n", "<br />")
        return output
    
    @cherrypy.expose()
    def echo(self, *args, **kwargs):
        return args[0]