#!/usr/bin/python3

import sys
import os.path
import re

summitpat = re.compile("chr([^:]+):([0-9]+)-[0-9]+__([^:]+):([^:]+):(.+)")

consensus = dict()
for i in open(sys.argv[1]):
	fields = i.rstrip().split("\t")
	consensus[fields[1]] = fields[0]

motifpos = dict()
for i in open(sys.argv[2]):
	fields = i.rstrip().split("\t")
	key    = fields[1] + ":" + fields[2] + ":" + fields[3] + ":" + fields[7]
	motifpos[key] = fields[0]

for name in sys.argv[3:]:
	if name == "../../motif_vs_summit_distances/factor/ZNF740_datatable.tbl":
		continue
	b = os.path.basename(name)
	motif = b.split("_")[0]
	if motif not in consensus:
		continue
	motifid = consensus[motif]
	f = open(name)
	for i in f:
		fields  = i.rstrip().split("\t")
		chrx    = fields[0].replace('chr', '')
		start   = fields[1]
		end     = fields[2]
		summits = fields[6].split(";")
		key     = chrx + ":" + start + ":" + end + ":" + motifid
		posid   = motifpos[key]

		for s in summits:
			match = summitpat.search(s)
			summitchr = match.group(1)
			summitpos = match.group(2)
			exp       = match.group(3)
			dist      = match.group(4)
			hight     = match.group(5)
			print(summitchr, summitpos, dist, hight, posid, exp)
	f.close()
