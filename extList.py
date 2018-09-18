#!/usr/bin/env python

import sys
from os import listdir
from os.path import isfile, join, isdir
import os

mypath = os.getcwd()

extDict = dict()

if len(sys.argv) > 1 :
	
	#tmpPath = os.path.realpath(sys.argv[1])
	if os.path.exists(os.path.realpath(sys.argv[1])):
		mypath = os.path.realpath(sys.argv[1])
	else:
		#mypath = os.path.expanduser("~")
		print "failed to get directory \nSeraching the current directory..."
else:
	print "usage :\n", __file__, "directoryToList"
	print "\n\n Seraching the current directory..."


try:
	
	filesindir = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	
	for filee in filesindir:
		ext = os.path.splitext(filee)[1].lower()
		if ext == "" :
			ext = os.path.splitext(filee)[0].lower()
		#print ext
		if ext in extDict:
			extDict[ext] += 1
		else:
			extDict[ext] = 1
			
	
	
	print "files {"
	for key, value in extDict.items():
		print key, value
	print "}"
except NameError:
	print "directory is not valid"
	sys.exit()
