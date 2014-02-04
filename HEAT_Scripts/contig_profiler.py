# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:46:38 2014

@author: nick
"""

#!/usr/bin/python

from Bio import SeqIO
import sys

def n_stat(lengths,prop):

    '''Example: N50 stat: n_stat(lengths, 0.5)'''
    
    index=0
    total=0
    while total<sum(lengths)*prop:
        total+=lengths[index]
        index+=1
    return lengths[index]

def contig_file_profile(filename):

    handle = open(filename)
    fasta_file=SeqIO.parse(handle, 'fasta')
    
    record_lengths=[]
    for record in fasta_file:
        record_lengths.append(len(record))    
        
    print "Total number of contigs: %d" % len(record_lengths)
    print "Total number of bases in all contigs: %d" % sum(record_lengths)    
    print "Largest contig: %d" % max(record_lengths)
    print "N50: %d" % n_stat(record_lengths, 0.5)
    print "N90: %d" % n_stat(record_lengths, 0.9)

def main(filename):
    contig_file_profile(filename)

#filename = sys.argv[1]
if __name__=="__main__":
    main(filename)

    
