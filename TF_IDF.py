from __future__ import division
import nltk
import math
import numpy
from nltk.corpus import stopwords
from math import log


def simple_tokenizer(komentar):
	data=[]
	for i, kalimat in enumerate(komentar):
		tokenisasi=nltk.word_tokenize(kalimat)
		data.append(tokenisasi)
	return data