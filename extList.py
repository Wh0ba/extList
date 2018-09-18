#!/usr/bin/env python

import sys
from os import listdir
from os.path import isfile, join
import os

mypath = os.path.realpath(sys.argv[1])

extDict = dict()

try:
	roms = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	gbaGames = 0
	gbcGames = 0
	for rom in roms:
		ext = os.path.splitext(rom)[1].lower()
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