#!/usr/env/python

from Bio import SeqIO
import sys

filename = sys.argv[1]

SeqIO.convert(filename, 'fastq', '%s%s' % (filename.split('.')[0],  '.fasta'), 'fasta')


