#!/bin/python

###The purpose of this script is to take a file of contigs, a mate-pair library, 
###and a blast database as input, and produce a pseudocontig as output. 

#####################
###Potential workflow
#####################

###Read end of contig
###Blast against mate pair library 1
###Parse blast output to get contig names
###Use an index to get the opposing mate pair
###Blat the opposing mate against the database of contigs
###Record the contigs that are associated with starting contig
###Use these associations to deduce the scaffold

#####################

###Imports

import Bio

###Read file of contigs

def parse_fasta(filename):
    handle = open(filename) 
    fasta_file=SeqIO.parse(handle, 'fasta') #Create a blast_record object

    records=[]
    for record in fasta_file:
        records.append(str(record))   #build a list with all of the sequences 

### Get samples from the ends of the contigs

#I haven't figured out what the best way to hold this data will be. 
#I think the choices are between a dictionary in memory or a file on disk.

#Using a dictionary:

def sample_to_dict(records, k): #take k bases from each end of the contig
    record_ends={}
    count=0
    for i in records:
        record_ends{str(count)}=(i,(i[:k], i[-k:])) #so entry "1" will be the seq, 
                                                    #followed by the ends in a tuple
        count+=1


