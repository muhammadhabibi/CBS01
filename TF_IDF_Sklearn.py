from sklearn.feature_extraction.text import TfidfVectorizer
import numpy


komentar_bersih = open('komentar_bersih.txt', 'r')
# print komentar_bersih
data = komentar_bersih.read().split('\n')
komen_bersih=[]
for komen in data:
	komen_bersih.append(komen)

vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(komen_bersih)
# idf = vectorizer.idf_
# print dict(zip(vectorizer.get_feature_names(), idf))
idf = vectorizer._tfidf.idf_
print dict(zip(vectorizer.get_feature_names(), idf))