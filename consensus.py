#!/usr/bin/python3

# Create consensus motif table from motif_info_final.tbl

import sys

f = open(sys.argv[1])
f.readline()

count = 1
for i in f:
	fields = i.rstrip().split()
	print(count, fields[0], fields[1], fields[2], fields[3], "/molbio/projects/summitdb/database_2018/motif_info/motif_logos/" + fields[0] + ".pdf", sep = "\t")
	count += 1
