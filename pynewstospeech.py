#!/usr/bin/python

import subprocess
import feedparser
from time import sleep

feed = feedparser.parse('http://feeds.reuters.com/reuters/oddlyEnoughNews?format=xml')
for entry in feed.entries:
	subprocess.call(["espeak", "-v", "english-us", "-s", "120", "-p", "80", str(entry.title)])
	sleep(2)
