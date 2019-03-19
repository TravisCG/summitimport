#!/usr/bin/python3

# This script creates the experiment table.
# usage: experiment.py antibody.tsv cellline.tsv genome.tsv Factor.tbl Cofactor.tbl

import sys

antibody = dict()
for i in open(sys.argv[1]):
	fields = i.rstrip().split("\t")
	antibody[fields[1]] = fields[0]

celline = dict()
for i in open(sys.argv[2]):
	fields = i.rstrip().split("\t")
	celline[fields[1]] = fields[0]

genome = dict()
for i in open(sys.argv[3]):
	fields = i.rstrip().split("\t")
	genome[fields[1]] = fields[0]

count = 1
for name in sys.argv[4:]:
	f = open(name)
	f.readline()
	for i in f:
		fields                                  = i.rstrip().split("\t")
		name                                    = fields[0]
		SRA_URL                                 = fields[1]
		is_it_paired_end                        = fields[2].upper()[0]
		sra_record_url                          = fields[3]
		if fields[6] == "":
			unique_pos                              = 0
			total_tags                              = 0
			fragment_estimate                       = 0
			peak_size_estimate                      = 0.0
			tags_per_BP                             = 0.0
			avg_tags_per_pos                        = 0.0
			avg_tag_length                          = 0.0
			avg_frag_GC                             = 0.0
			total_peaks                             = 0
			peak_size                               = 0
			total_tags_in_peaks                     = 0.0
			expected_tags_per_peak                  = 0.0
			putative_peaks                          = 0
			putative_peaks_filtered_by_local_signal = 0
			putative_peaks_filtered_too_clonal      = 0
			peaks_after_filtering                   = 0

		else:
			unique_pos                              = int(fields[6])
			total_tags                              = int(fields[7])
			fragment_estimate                       = int(fields[8])
			peak_size_estimate                      = float(fields[9])
			tags_per_BP                             = float(fields[10])
			avg_tags_per_pos                        = float(fields[11])
			avg_tag_length                          = float(fields[12])
			avg_frag_GC                             = float(fields[13])
			total_peaks                             = int(fields[14])
			peak_size                               = int(fields[15])
			total_tags_in_peaks                     = float(fields[16])
			expected_tags_per_peak                  = float(fields[17])
			putative_peaks                          = int(fields[18])
			putative_peaks_filtered_by_local_signal = int(fields[19])
			putative_peaks_filtered_too_clonal      = int(fields[20])
			peaks_after_filtering                   = int(fields[22])
			antibody_field                          = fields[24]

		if antibody_field == "cofactor":
			exp_type = "cofactor"
		else:
			exp_type = "factor"

		Genome_genome_id                        = genome[name[:2]]
		nf = name.split("_")
		Cell_lines_celline_id                   = celline[nf[2]]
		if nf[4] not in antibody:
			Antibody_antibody_id            = "0"
		else:
			Antibody_antibody_id            = antibody[nf[4]]

		print(count, name, SRA_URL, is_it_paired_end, sra_record_url, unique_pos, total_tags, fragment_estimate, peak_size_estimate, tags_per_BP, avg_tags_per_pos, avg_tag_length, avg_frag_GC, total_peaks, peak_size, total_tags_in_peaks, expected_tags_per_peak, putative_peaks, putative_peaks_filtered_by_local_signal, putative_peaks_filtered_too_clonal, peaks_after_filtering, exp_type, Genome_genome_id, Cell_lines_celline_id, Antibody_antibody_id, sep = "\t")

		count += 1
	f.close()
