import random


class Complex_Sequence():
    """This Class will contain our sequence and some methods to mess with it"""
    def __init__(self, seq):
        self.seq = seq
        self.rc=self.revcomp(seq)
    
    def revcomp(self, seq):
        """This method will produce the reverse complement of the sequence"""
        
        complement=[] #New list to hold the complementary strand (more memory efficient
                      #than string concatenation over and over again. 

        comp={'A':'T', 'T':'A', 'G':'C', 'C':'G'} #This is a dictionary of complementary
                                                  #bases to make the comp strand. 

        for i in seq:
            complement.append(comp[i]) #Add the complementary base for each base in the seq
       
        complement_string=''.join(complement) #Join the list together ONCE

        return complement_string[::-1] #Slice the string with a -1 seperator to get the 
                                       #reverse of the string


    def splitter(self, seq):
        """This method will split the sequence into lists of words and store them as 
        attributes of the main class"""
    
        ###Rationale: The larger the word, the higher the complexity will inherently be because
        ###there will be a much lower chance of getting the same sequence. I think that a word
        ###size of 2, 3, or 4 would be reasonable. We should try these three word sizes and plot
        ###the resulting output. 

        ###We should also consider multiple reading frames. 

        #Reading frame 1
        self.rf1=[]
        i=0
        while i < len(seq)-length_of_word:
            self.rf1.append(seq[i:i+length_of_word])
            i+=length_of_word
        self.rf1.append(seq[i:])

        
        
def main():
    """The main routeine of the program"""
        
    seq1=''

    #Generate a random DNA Sequence
    for i in range(20):
        seq1+=random.choice(['A', 'T', 'G', 'C'])
    
    
    comp1=Complex_Sequence(seq1)
    print comp1.seq
    print comp1.rc
    
    comp1.splitter(seq)
    print comp1.rf1

if __name__=="__main__":
    main()
















e__=="__main__":
    main()
