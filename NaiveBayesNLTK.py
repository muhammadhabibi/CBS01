from nltk.probability import ELEProbDist, FreqDist
import nltk
import Preprocessing
import json
import yaml

pp = Preprocessing


#memanggil file komentar json
output_file = open('komentar.json').read()
#komentar = json.loads(output_file)
#untuk menghilangkan u'coba'
komentar = yaml.safe_load(output_file) 

data_komentar=[]
for i, komen in enumerate(komentar):
	tup=()
	data1=(komentar[i][3])
	data2=(komentar[i][5])
	tup=(data1,data2)
	data_komentar.append(tup) #list of Tuple

# print data_komentar

# data = pp.pre_processing(data_komentar)
# print data

# Membuat list tuple pelatihan dan penyaringan dua huruf kata
komentars = []
for (words, sentiment) in data_komentar:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    komentars.append((words_filtered, sentiment))


# mencari frekuensi kata dari data pelatihan
def get_words_in_komentar(komentars):
    all_words = []
    for (words, sentiment) in komentars:
      all_words.extend(words)
    return all_words

#mencari daftar kata2 yang berbeda
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


#membuat extracttor feature / kamus
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# def train(labeled_featuresets, estimator=ELEProbDist):
#      # Create the P(label) distribution
#     label_probdist = estimator(label_freqdist)
#     # Create the P(fval|label, fname) distribution
#     feature_probdist = {}
#     return NaiveBayesClassifier(label_probdist, feature_probdist)





#data testing
test_komentar=[]
test_komentar.append("Buku rujukan kurang jelas mau pakai yang mana")
test_komentar.append("Penyampaian materi terlalu lemah lembut")
test_komentar.append("saya senang dengan pembelajaran ini")
test_komentar.append("saya suka dengan pembelajaran fismod karena tidak terpacu rumus")

word_features = get_word_features(get_words_in_komentar(komentars))

#membangun set training
training_set = nltk.classify.apply_features(extract_features, komentars)

#melatih Klasifier
classifier = nltk.NaiveBayesClassifier.train(training_set)


#untuk menampilkan informasi feature
print classifier.show_most_informative_features(32)

#testing klasifier
for test in test_komentar:
	#untuk melihat feature kata apa aja yang dianggap benar/True
	print (test, classifier.classify(extract_features(test.split())))
	# print extract_features(test.split())

