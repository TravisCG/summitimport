#!/usr/bin/python3

"""
   The script reads all the homer peak files and creates the peak table. The first argument is the experiment table,
   because the script needs the foreign key
"""

import sys
import os.path

experiment = dict()
for i in open(sys.argv[1]):
	fields = i.rstrip().split("\t")
	experiment[fields[1]] = fields[0]

count = 1
for name in sys.argv[2:]:
	b = os.path.basename(name)
	exp = b.replace('_homerpeaks.txt', '')
	if exp not in experiment:
		continue
	f = open(name)
	for i in f:
		if i.startswith('#'):
			continue
		fields              = i.rstrip().split("\t")
		chrx                = fields[1].replace('chr', '')
		start               = int(fields[2])
		end                 = int(fields[3])
		norm_tag_count      = float(fields[5])
		focus_ratio         = float(fields[6])
		findPeaks_score     = float(fields[7])
		foldchange_vs_local = float(fields[8])
		pvalue              = float(fields[9])
		clonal_foldchange   = float(fields[10])

		print(count, chrx, start, end, norm_tag_count, focus_ratio, findPeaks_score, foldchange_vs_local, pvalue, clonal_foldchange, experiment[exp], sep = "\t")
		count += 1
	f.close()
