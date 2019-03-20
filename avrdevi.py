#!/usr/bin/python3

import sys
import os.path

experiment = dict()
for i in open(sys.argv[1]):
	fields = i.rstrip().split("\t")
	experiment[fields[1]] = fields[0]

consensus = dict()
for i in open(sys.argv[2]):
	fields = i.rstrip().split("\t")
	consensus[fields[1]] = fields[0]

count = 1
for name in sys.argv[3:]:
	b = os.path.basename(name)
	motif = b.split("_")[1]
	f = open(name)
	f.readline()
	for i in f:
		fields   = i.rstrip().split("\t")
		exp      = fields[0]
		parts    = exp.split("_")
		cellline = parts[2]
		antibody = parts[4]
		srx      = parts[5]
		avgname  = "Motif: %s - Antibody: %s - Cell Type: %s - Experiment: %s" % (motif, antibody, cellline, srx)
		if exp not in experiment:
			continue
		if motif not in consensus:
			continue
		print(count, fields[1], fields[2], fields[3], fields[4], experiment[exp], consensus[motif], avgname, sep = "\t")
		count += 1
	f.close()
