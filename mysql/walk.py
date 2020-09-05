#!/usr/bin/python

import os

rootDir = '/home/stef'
for dirName, subdirList, fileList in os.walk(rootDir):
	print('Found directory: %s' % dirName)
	for fname in fileList:
		print('\t%s' % fname)
