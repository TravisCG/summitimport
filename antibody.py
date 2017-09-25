#!/usr/bin/python3

# create antibody table
# read the two experiment tables where the 4th part of the experiment name is the antibody

import sys

antibody = set()

for fn in sys.argv[1:]:
	f = open(fn)
	f.readline() # header
	for i in f:
		a = i.rstrip().split()[0].split("_")[4]
		antibody.add(a)
	f.close()

count = 1
for a in antibody:
	print(count, a, sep = "\t")
	count += 1
