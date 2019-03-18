#!/usr/bin/python3

import glob
import sys

db = glob.glob(sys.argv[1] + "/*.meme")

out = open("pfm.tsv", "w")
for i in db:
    matrixfile = open(sys.argv[1] + "/" + i)
    counter = 0
    for j in matrixfile:
        mfields = j.rstrip().split()
        if len(mfields) == 4:
            counter = counter + 1
            out.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (motifid, counter, mfields[0], mfields[1], mfields[2], mfields[3]))
    matrixfile.close()
out.close()
