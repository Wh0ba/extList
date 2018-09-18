#!/usr/bin/env python

import sys
from os import listdir
from os.path import isfile, join
import os

mypath = os.path.dirname(os.path.abspath(__file__))

extDict = dict()
if len(sys.argv) > 1 :
	
	#tmpPath = os.path.realpath(sys.argv[1])
	if os.path.exists(os.path.realpath(sys.argv[1])):
		mypath = os.path.realpath(sys.argv[1])
	else:
		#mypath = os.path.expanduser("~")
		print "failed to get directory \nSeraching the current directory..."
		mypath = os.path.dirname(os.path.abspath(__file__))
else:
	print "Seraching the current directory..."

try:
	
	filesindir = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	
	for filee in filesindir:
		ext = os.path.splitext(filee)[1].lower()
		#print ext
		if ext in extDict:
			extDict[ext] += 1
		else:
			extDict[ext] = 1
			
		
	
	
	for key, value in extDict.items():
		print key, value
except NameError:
	print "directory is not valid"
	sys.exit()
