import Bio.SeqIO
import random

starter_string=''


def randomSeqGenerator(length):

	'''This function generates a string that should have a complexity near 1. We are defining complexity as the number of occurrences of the current word divided by the number of total words, and this string is composed of completely random words.'''
 
	for i in range(length):
		starter_string+=random.choice(['A', 'T', 'G', 'C'])

def sequenceSplitter():

	'''This function will break a string into a bunch of words in a list, which can be used by another function to compute the complexity.'''

	#For DNA, we will potentially want to split the string up to 6 ways. I am not yet sure what effect splitting the string only once would have on the complexity. Also, the word size is a variable that we will have to play around with. 

	list_plus1=[]
	list_plus2=[]
	list_plus3=[]
	list_minus1=[]
	list_minus2=[]
	list_minus3=[]

	#Maybe this would be agood place to play with object oriented code? What will this function return? A bunch of lists would be not good, because then the function call will have to explicitely declare a handle for all of the returned variables. We could return a dictionary or list of lists, but that might not be as nice as returning an object. In fact, we could have this splitting function as a method of a class. 


