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

def main(index, hit_names, export_file_name):
    globals().update(index, hit_names)
    SeqLookup(index, hit_names, export_file_name)

###############################################################################

if __name__=='__main__':
    main(globals()['index'], globals()['hit_names'], '/home/nick/Desktop/QueryA_exportseqs.fasta') 
    #leave the index and hit names as long as your handle for your index is called
    #'index.' Change the filename to the desired export file name. 
    
###############################################################################