#!/usr/bin/python3

# Create cell lines table

import sys

cellline = set()

for fn in sys.argv[1:]:

	f = open(fn)
	f.readline()

	for i in f:
		expname = i.rstrip().split()[0]
		fields  = expname.split("_")
		cl      = fields[2]
		if cl.upper() == "CELLLINE":
			cl = 'UNKNOWN'
		cellline.add(cl.upper())

	f.close()

count = 1
for cl in cellline:
	print(count, cl, sep = "\t")
	count += 1
