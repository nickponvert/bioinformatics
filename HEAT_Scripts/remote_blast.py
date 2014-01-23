#This script takes the query sequences we generate with the slicer
#and blasts them against a database

from Bio.Blast.Applications import NcbiblastnCommandline

query='/home/nick/Desktop/QueryA.fasta'
db='/home/nick/Documents/MTF9_Data/Sync/MTF9_1.fasta'
out='/home/nick/Desktop/QueryA_out.xml'

blast_cline=NcbiblastnCommandline(query=query
                                  ,db=db
                                  ,outfmt=5
                                  ,out=out
                                  )

stdout, stderr=blast_cline()