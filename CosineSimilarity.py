from __future__ import division
import nltk
import math
import numpy

def TFIDF(document):
	dokumen=''
	kum_kata=set()
	for dokumen in document:
		kum_kata=kum_kata.union(set(dokumen.split(' '))) #proses penggabungan
	kum_kata=sorted(kum_kata)
	collection = nltk.TextCollection(kum_kata) #mengurutkan kumpulan kata berdasarkan abjad
	unique_terms = list(collection) #print list(collection)
	word_tfidf = []
	for word in unique_terms:
		word_tfidf.append(collection.tf_idf(word,document))
	# file = open("TF_IDF.txt", "wb")
	# file.write("%s " %kum_kata + "%s\n" %word_tfidf)
	# file.close()
	return word_tfidf
    
def sum_of_squares(vector): #menghitung nilai Vector
	sum = 0
	for i in vector:
		sum += i*i
	return sum
    
def similarity(input_vector,text):
	sum = 0
	for x,y in zip(input_vector,text):
		sum += (x*y)
		
	return (sum / (math.sqrt(sum_of_squares(input_vector)*sum_of_squares(text))))

