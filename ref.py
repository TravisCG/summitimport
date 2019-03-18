#!/usr/bin/python3

import gzip

seq = []
out = open("reference.tsv", "w")
for i in gzip.open("Homo_sapiens.GRCh37.dna.primary_assembly.fa.gz", "r"):
    line = i.decode('utf-8').rstrip()
    if line.startswith(">"):
        if len(seq) > 0:
            seq = "".join(seq)
            for j in range(0, len(seq), 200):
                subseq = seq[j:j+200]
                if subseq == "N"*200:
                    continue
                out.write("%s\t%d\t%d\t%s\n" % (header, j+1, j+len(subseq), subseq))
        seq = []
        header = line.split()[0][1:]
        if header.startswith('K') or header.startswith('G'): # alternative contigs
            break
        continue
    seq.append(line)
out.close()
