from Bio import SeqIO
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline

__all__=['Sequence_Sampler', 'BLAST', 'Blast_Parser', 'indexer', 'SeqLookup']

def help():
    print '''

HEAT Genomics Tools v0.1

This module contains scripts that have proven useful for analysis of paired-end sequence data. 
The following functions are currently included:

blast(query, db, out): Sets up and runs a local BLAST query using the NcbiblastnCommandline tool. Returns an
XML file for use with the BLAST parser.

blast_mate_parser(results_file): Takes an XML BLAST report and returns the names of all of the hits in the report. 
This is useful for mate-pair analysis because it allows us to BLAST a fasta file containing some samples against 
one of the mate-pair databases and parse out the names of all of the mate-pairs that have an end in the sampling
region.

sequence_sampler(sequence): Currently set up to return 40b samples from the end of a sequence, walking in to the 
sequence in 200b increments.

seq_lookup(index, hit_names, export_file_name): Accepts a list of hit names and searches for the opposing mate pair sequence in an 
indexed fasta file. Writes the sequences to a file in FASTA format. 
'''

def blast(query, db, out):
    
    '''BLAST the sample file created by Sequence Sampler against a db of your choosing, 
    return an .xml results file in the current directory'''
    
    blast_cline=NcbiblastnCommandline(query=query, db=db, out=out, outfmt=5)
    blast_cline()    

def blast_mate_parser(results_file):
    
    '''Get all of the hit names from one or more queries\n\n
    Example Usage: hit_names=Blast_Parser(results_file)
    '''
    
    result_handle=open(results_file)
    records_1=NCBIXML.parse(result_handle)
    hit_names=[]

    for record in records_1:
        for alignment in record.alignments:
            align_name_split=str(alignment.title).split(' ')
            hit_names.append(align_name_split[1])
    
    return hit_names

#The function below will be critical for building an application using these tools, beacuse it allows us to index
#a huge fasta file as an SQL database instead of as an object 

# def indexer(index_name):
    
#     '''Set up an index to search a large fasta file. We are going to try to use the SeqIO.index_db
#     because it creates (and subsequently loads) a SQLite database on disk instead of a giant
#     2GB thing in memory.'''
    
#     index=SeqIO.index_db(index_name, 'fasta')
#     return index

def sequence_sampler(sequence, sample_file_name):
    
    '''Make a file in the current directory that contains a bunch of 40b samples from the end of a sequence'''
    
    sample_file=open(sample_file_name, 'w')
    for i in range(-200, -2400, -200):
        sample=sequence[i:i+40]
        sample_file.write('>Sample%d\n%s\n\n' % (i, str(sample)))

def seq_lookup(index, hit_names, export_file_name):

    '''Accepts a list of sequence names generated by blast_mate_parser and returns the other end of the mate-pair. Recovered mate
    sequences are stored in an export file in fasta format. The export file will be saved in the current directory unless specified
    in the export file name.'''

    #First we open a file to save our results to
    export_file=open(export_file_name, 'w')

    #set up some lists to keep track of things
    not_found=[]
    found=[]

    #Iterate over every one of the names in the list of hit names
    for i in range(len(hit_names)):

    #The try/except language allows us to keep everything going even if we get an error from trying to search for a nonexistant 
    #sequence name in the index. 

    ##UPDATE: The blast_mate_parser function has been updated to work properly, so we are no longer running into this problem. 
    ##However, the use of try/except allows this function to handle problems more gracefully and report the sequences that were
    ##not found, so it is being left as-is. 

        try:
            seq=index[hit_names[i]].seq #This searches the index for the sequence

            seqname=index[hit_names[i]].id #This is the name of the sequence in the index

            export_file.write('>1-2-%s\n%s\n\n' % (str(seqname), str(seq))) #This writes the ID and sequence to the export file in FASTA form.
        
            found.append(seqname) #Keep a record of all the sequences for which we are able to find a mate.

        #A KeyError is raised if we try to ask the index for something it doesn't think it has. I am not sure
        #why we are not able to find some sequences in the file while some work out just fine. However, this 
        #allows us to record the names of the sequences that we can't find for some reason. 
        except KeyError:
            not_found.append(hit_names[i])

    print "%d out of %d sequences found" % (len(found), len(hit_names)) #How many sequences are we able to recover?

    #all the sequences will now be available in the export file. 
    export_file.close()