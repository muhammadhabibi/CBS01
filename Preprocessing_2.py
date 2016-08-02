from __future__ import division
import nltk
import math
import numpy
from nltk.stem.porter import *
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def pre_processing(doc):
	kata = ""
	datas ={}

	#stemming Sastrawi
	factory = StemmerFactory()
	stemmer = factory.create_stemmer()

	#proses Stopword removal dan tokenisasi
	for index, kalimat in enumerate(doc):
		data = []
		dataku=[]
		#membuat kalimat menjadi token/terpisah menggunakan NLTK
		tokenisasi = nltk.word_tokenize(kalimat)
		# stopWords = nltk.corpus.stopwords.words('english') + ['yang','dengan']
		# memanggil corpus daftar kalimat yang akan dihapus dari file stopwords.txt
		stopwords = open('stopwords.txt', 'r').read().split()
		for idx, word in enumerate(tokenisasi):
			# jika kata dalam komentar tidak dalam corpus stopwords.txt
			if word not in stopwords:
				# maka kata dimasukkan kedalam data
				kata = " "+word
				data.append(stemmer.stem(kata))
		datas[index] = " ".join(data)
		dataku=" ".join(data)
		# jika kata ada dalam stopwords.txt, maka kata dihapus atau dikosongkan
		kata = ""
		file = open("komentar_bersih.txt", "a")
		file.write("(%s" %index + ", %s),\n" %dataku)
		file.close()
	# membuat file untuk menyimpan data komentar yang sudah bersih
	
	return datas