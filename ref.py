#!/usr/bin/python3

import gzip
import sys

seq = []
for i in gzip.open(sys.argv[1], "r"):
    line = i.decode('utf-8').rstrip()
    if line.startswith(">"):
        if len(seq) > 0:
            seq = "".join(seq)
            for j in range(0, len(seq), 200):
                subseq = seq[j:j+200]
                if subseq == "N"*200:
                    continue
                print("%s\t%d\t%d\t%s" % (header, j+1, j+len(subseq), subseq))
        seq = []
        header = line.split()[0][1:]
        if header.startswith('K') or header.startswith('G'): # alternative contigs
            break
        continue
    seq.append(line)
