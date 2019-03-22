#!/usr/bin/python3

# create antibody table
# read the two experiment tables where the 4th part of the experiment name is the antibody

import sys

antibody = dict()

f = open(sys.argv[1])
f.readline() # header
for i in f:
	a = i.rstrip().split()[0].split("_")[4]
	antibody[a] = list()
f.close()

f = open(sys.argv[2])
f.readline()
for i in f:
	fields = i.rstrip().split("\t")
	if fields[0] not in antibody:
		continue
	antibody[fields[0]] = fields
count = 1
for a in antibody:
	print(count, "\t".join(antibody[a]), sep = "\t")
	count += 1
