#!/usr/bin/python3

import sys

consens = dict()
for i in open(sys.argv[1]):
	fields = i.rstrip().split()
	consens[fields[1]] = fields[0]

antibody = dict()
for i in open(sys.argv[2]):
	fields = i.rstrip().split()
	antibody[fields[1]] = fields[0]

cmf = open(sys.argv[3])
cmf.readline()
for i in cmf:
	fields = i.rstrip().split("\t")
	motif_name = fields[0]
	antibodies = fields[4].split(",")
	for a in antibodies:
		if a in antibody:
			print(antibody[a], consens[motif_name], sep = "\t")
