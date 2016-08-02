#!C:/python27/python.exe
from __future__ import division
import math
import numpy
import nltk
import json
import yaml
import Preprocessing
import TF_IDF
import CosineSimilarity

pp = Preprocessing
cs = CosineSimilarity

#memanggil file komentar json
output_file = open('komentar.json').read()
#komentar = json.loads(output_file)
#untuk menghilangkan u'coba'
komentar = yaml.safe_load(output_file) 

# data_komentar=[]
# for i, komen in enumerate(komentar):
# 	data_komentar.append(komentar[i][3])
# # print data_komentar

# data = pp.pre_processing(data_komentar)
# print data

# ------------------------------------------------------------
komentar_bersih = open('komentar_bersih.txt', 'r')
# print komentar_bersih
data = komentar_bersih.read().split('\n')
komen_bersih=[]
for komen in data:
	komen_bersih.append(komen)

# menghitung Cosine Similarity
vector = [cs.TFIDF(t) for t in komen_bersih]
kalimat=[]
kalimat.append("sebaiknya waktu kuliahnya jangan terlalu sore")
kalimat.append("lebih keras lagi suara")
kalimat.append("buku rujuk kurang jelas mau pakai mana")


#Data testing
for test in kalimat:
	print'---------------------------------------------------------------------------------------'
	print'Data Testing :', test
	input_vector = cs.TFIDF(nltk.Text(str(test)))
	Hasil=[]
	tup=()
	for i,t in enumerate(vector):
		sim = cs.similarity(input_vector,t)
		nilai_sim=sim
		komentars=komen_bersih[i]
		tup=(i,nilai_sim,komentars)
		Hasil.append(tup)
	
	#mengurutkan hasil cosine similarity ascending, menampilkan nilai tertinggi dgn index 0
	Hasil_sim=sorted(Hasil, key=lambda x: x[1], reverse=True)[0]
	print Hasil_sim
	print ("------------------------------------------------------------------------")

	#untuk memberi nilai threshold / batas
	for (index, cosine, kal) in Hasil:
		if cosine >= 0.93 :
			print (cosine, kal)





