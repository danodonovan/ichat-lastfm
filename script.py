#!/usr/bin/env python
# encoding: utf-8¬
"""
lastfm-ichat.py

Created by Daniel O'Donovan on 2012-01-04.
Copyright (c) 2012. All rights reserved.
"""

import sys
import urllib2
import contextlib
from BeautifulSoup import BeautifulSoup
from subprocess import call
import tempfile

# Set last.fm username here
username = 'yourusername'

rss_url = "http://ws.audioscrobbler.com/2.0/user/%s/recenttracks.rss" % username

with contextlib.closing(urllib2.urlopen(rss_url)) as u:
   rss_data = u.read()

soup = BeautifulSoup(rss_data)

try:
    message = soup.findAll("title")[1].text
except:
    sys.exit()

message = u'♫ ' + message

osascript = """
set message to "%s"
tell application "System Events"
    if exists process "iChat" then tell application "iChat" to set the status message to message
end tell""" % message

# if exists process "Adium" then tell application "Adium" to set status message of every account to message            
# print osascript

# with tempfile.NamedTemporaryFile() as f:
#     f.write(osascript)

sts = call(["/usr/bin/osascript", "-e", osascript], shell=False)

