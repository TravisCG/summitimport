#!/usr/bin/python3

import glob
import sys

db = open(sys.argv[1])

for i in db:
    fields = i.rstrip().split()
    motifid = fields[0]
    motifname = fields[1]
    matrixfile = open(sys.argv[2] + "/" + motifname + ".meme")
    counter = 0
    for j in matrixfile:
        mfields = j.rstrip().split()
        if len(mfields) == 4:
            counter = counter + 1
            print("%s\t%s\t%s\t%s\t%s\t%s" % (motifid, counter, mfields[0], mfields[1], mfields[2], mfields[3]))
    matrixfile.close()
