#!/usr/env/python

from Bio import SeqIO
import sys

def convert_fastq(file):

	'''This function takes a fastq file and creates a converted fasta file in the same directory, with the same filename'''

	SeqIO.convert(file, 'fastq', '%s.%s' % (file.split('.')[0], 'fasta'), 'fasta')


