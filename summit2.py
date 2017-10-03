#!/usr/bin/python3

import sys

def selectpeak(array, lowindex, hiindex, expid, testpos, fields):
	if testpos < array[lowindex][1] or testpos > array[hiindex][2]:
		return
	midindex = int(lowindex + (hiindex - lowindex) / 2)

	if hiindex - lowindex < 4:
		i = lowindex
		while testpos > array[i][1] and i < len(array)-1:
			if testpos > array[i][1] and testpos < array[i][2] and expid == array[i][3]:
				print(fields[0], fields[1], fields[2], fields[3], fields[4], array[i][0], sep = "\t")
			i += 1
		return

	if testpos > array[lowindex][1] and testpos < array[midindex][2]:
		selectpeak(array, lowindex, midindex, expid, testpos, fields)
	elif testpos > array[midindex][1] and testpos < array[hiindex][2]:
		selectpeak(array, midindex, hiindex, expid, testpos, fields)

selectedchr = sys.argv[1]

peaks = list()
for i in open(sys.argv[2]):
	fields = i.rstrip().split("\t")
	peakid = fields[0]
	chrx   = fields[1]
	if chrx != selectedchr:
		continue
	start  = int(fields[2])
	end    = int(fields[3])
	expid  = fields[10]

	peaks.append([peakid, start, end, expid])

peaks = sorted(peaks, key = lambda x:x[1])

experiment = dict()
for i in open(sys.argv[3]):
	fields = i.rstrip().split("\t")
	experiment[fields[1]] = fields[0]

for i in open(sys.argv[4]):
	fields = i.rstrip().split()
	if fields[5] not in experiment:
		continue
	if fields[0] != selectedchr:
		continue
	expid = experiment[fields[5]]
	pos   = int(fields[1])
	selectpeak(peaks, 0, len(peaks)-1, expid, pos, fields)
