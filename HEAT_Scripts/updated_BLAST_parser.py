from Bio.Blast import NCBIXML

def Blast_Parser(results_file):
    
    '''Get all of the hit names from one or more queries'''
    
    result_handle=open(results_file)
    records_1=NCBIXML.parse(result_handle)
    hit_names=[]

    for record in records_1:
        for alignment in record.alignments:
            align_name_split=str(alignment.title).split(' ')
            hit_names.append(align_name_split[1])
            #print align_name_split[1]
    
    return hit_names

def main(results_file):
    hit_names=Blast_Parser(results_file)
    return hit_names


######################################################################
# Enter the name of the .xml file from the BLAST search below and hit 
# the run button. This will save the names of the hits in the variable
# called hit_names. 

if __name__=='__main__':
    hit_names=main('/home/nick/Desktop/QueryA_out.xml') #Just change this line
                                                        #to the name of the results
                                                        #file and run.

######################################################################
    