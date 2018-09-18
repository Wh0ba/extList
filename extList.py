#!/usr/bin/env python

import sys
from os import listdir
from os.path import isfile, join
import os

mypath = os.path.realpath(sys.argv[1])

extDict = dict()

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
	print mypath
	print "directory is not valid"
	sys.exit()
