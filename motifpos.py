#!/usr/bin/python3

import sys
import os.path

consensus = dict()
for i in open(sys.argv[1]):
	fields = i.rstrip().split("\t")
	consensus[fields[1]] = fields[0]

count = 1
for name in sys.argv[2:]:
	b = os.path.basename(name)
	motif = b.split("_")[0]
	f = open(name)
	f.readline()
	for i in f:
		fields = i.rstrip().split("\t")
		chrx   = fields[0].replace('chr', '')
		start  = int(fields[1])
		end    = int(fields[2])
		strand = fields[5]
		hscore = fields[4]
		if (end - start) % 2 == 0:
			trivial = "F"
		else:
			trivial = "T"
		if motif not in consensus:
			continue
		print(count, chrx, start, end, strand, hscore, trivial, consensus[motif], sep = "\t")
		count += 1
	f.close()
