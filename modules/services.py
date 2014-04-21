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
import re


logger = logging.getLogger('modules.services')

class Services:
    def __init__(self):
        self.logger = logging.getLogger('modules.services')
        htpc.MODULES.append({
                'name': 'Misc Services',
                'id': 'services',
                'fields': [
                    {'type': 'bool', 'label': 'Enable', 'name': 'services_enable'},
                    {'type': 'text', 'label': 'Menu name', 'name': 'services_name'},
                    {'type': 'text', 'label': 'Plex IP / Host *', 'name': 'plex_host'},
                    {'type': 'text', 'label': 'Library # *', 'name': 'libraryID'}
        ]})
    
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
        host = htpc.settings.get('plex_host','')
        library = htpc.settings.get('libraryID', '')
        import subprocess
        temp = subprocess.check_output("python /opt/autodelete.py -i "+ host + " -s " + library, shell=True)
        output = temp.replace("\n", "<br />")
        return output
    
    @cherrypy.expose()
    def deletewatchedplex(self, *args):
        D = args[0]
        host = htpc.settings.get('plex_host','')
        library = htpc.settings.get('libraryID', '')
        import subprocess
        temp = subprocess.check_output("python /opt/autodelete.py -i " + host + " -d " + D + " -s " + library, shell=True)
        output = temp.replace("\n", "<br />")
        return output
    
    @cherrypy.expose()
    def echo(self, *args, **kwargs):
        return args[0]

    @cherrypy.expose()
    def getiotop(self):
        import subprocess
        temp = subprocess.check_output("iotop -o -n 1 -b", shell=True)
        #temp2 = temp.replace("\n", "<br />")
        temp2 = "<table border='1'><tr><td>" + re.sub(' +',' ',temp).replace(" ", "</td><td>") + "</td></tr></table>"
        output = temp2.replace("\n", "<br/>").replace("<br/></td>", "</td></tr><tr>").replace("</td><td>M/s", "M/s").replace("</td><td>K/s","K/s").replace("</td><td>B/s","B/s").replace("DISK</td><td>WRITE", "Disk Write").replace("DISK</td><td>READ", "Disk Read").replace("</td><td>%", "%").replace("Total</td><td>Disk", "Total Disk")
        return output