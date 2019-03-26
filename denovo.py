#!/usr/bin/python3

import sys

count = 1

for i in sys.argv[1:]:
	f = open(i)
	f.readline()
	for line in f:
		fields = line.rstrip().split()
		consensus = fields[4].replace('et', '')
		known_motif_finding = fields[5]
		print(count, consensus, count, known_motif_finding, sep = "\t")
		count += 1
	f.close()
