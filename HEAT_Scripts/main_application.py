from Bio.Blast.Applications import NcbiblastnCommandline


query='/home/nick/Desktop/QueryA.fasta'
db='/home/nick/Documents/MTF9_Data/Sync/MTF9_1.fasta'
out='/home/nick/Desktop/QueryA_out.xml'

def remote_blast(query, db, out)

'''Take a list of query sequences and BLAST them against a 
local database. Arguments are absolute paths to the files'''

    blast_cline=NcbiblastnCommandline(query=query
                                     ,db=db
                                     ,outfmt=5
                                     ,out=out
                                     )

    stdout, stderr=blast_cline()
    return stdout, stderr

