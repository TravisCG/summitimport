#!/usr/bin/python3

import sys

for i in sys.argv[1:]:
	f = open(i)
	for line in f:
		fields = line.rstrip().split("\t")
		chrx   = fields[0]
		exps   = fields[6].split(";")
		for e in exps:
			mchr = e.split(":")[0]
			if mchr != chrx:
				print(mchr, chrx)
	f.close()
