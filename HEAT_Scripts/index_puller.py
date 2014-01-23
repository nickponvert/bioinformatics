from Bio import SeqIO
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline

def Sequence_Sampler(sequence):
    
    '''Make a file in the current directory that contains a bunch of 40b samples from the end of a sequence'''
    
    sample_file=open('sample_file.fasta', 'w')
    for i in range(-200, -2400, -200):
        sample=sequence[i:i+40]
        sample_file.write('>2-Sample%d\n%s\n\n' % (i, str(sample)))

def BLAST(db):
    
    '''BLAST the sample file created by Sequence Sampler against a db of your choosing, 
    return an .xml results file in the current directory'''
    
    blast_cline=NcbiblastnCommandline(query='sample_file.fasta', db=db, out='Sample_Blast_Output.xml', outfmt=5)
    blast_cline()    

def Blast_Parser(results_file):
    
    '''Get all of the hit names from one or more queries'''
    
    result_handle=open(results_file)
    records_1=NCBIXML.parse(result_handle)
    hit_names=[]

    for record in records_1:
        for alignment in record.alignments:
            align_name_split=str(alignment.title).split(' ')
            hit_names.append(align_name_split[1])
    
    return hit_names

def indexer(index_name):
    
    '''Set up an index to search a large fasta file. We are going to try to use the SeqIO.index_db
    because it creates (and subsequently loads) a SQLite database on disk instead of a giant
    2GB thing in memory.'''
    
    index=SeqIO.index_db(index_name, 'fasta')
    return index

def SeqLookup(index, hit_names, export_file_name):
    #First we open a file to save our results to
    export_file=open(export_file_name, 'w')

    #set up some lists to keep track of things
    not_found=[]
    found=[]

    #Iterate over every one of the names in the list of hit names
    for i in range(len(hit_names)):

    #The try/except language allows us to keep everything going even if we get an error from trying to search for a nonexistant 
    #sequence name in the index. 

        try:
            seq=index[hit_names[i]].seq #This searches the index for the sequence

            seqname=index[hit_names[i]].id #This is the name of the sequence in the index

            export_file.write('>2-%s\n%s\n\n' % (str(seqname), str(seq))) #This writes the ID and sequence to the export file in FASTA form.
        
            found.append(seqname) #Keep a record of all the sequences for which we are able to find a mate.

        #A KeyError is raised if we try to ask the index for something it doesn't think it has. I am not sure
        #why we are not able to find some sequences in the file while some work out just fine. However, this 
        #allows us to record the names of the sequences that we can't find for some reason. 
        except KeyError:
            not_found.append(hit_names[i])

    print "%d out of %d sequences found" % (len(found), len(hit_names)) #How many sequences are we able to recover?

    #all the sequences will now be available in the export file. 
    export_file.close()

def main(blast_results, index_name, export_file_name):
 
 #The first step is to either create a SQLite index of a mate-pair library or to load one already 
 #in existance. The SeqIO.index_db function allows us to do precisely this. 


 #After we have our index ready to go, we need to get our file of contigs that we wish to examine. 
 #The file will contain many (possibly hundreds) of contigs and we need to 

blast_results='/home/nick/Desktop/QueryA_out.xml'
index_name='/home/nick/Documents/MTF9_Data/Sync/MTF9_2.fasta'
export_file_name="/home/nick/Desktop/MTF9_2_exportSeqs.fasta"

if __name__=='__main__':
    main(blast_results, index_name, export_file_name)


    
