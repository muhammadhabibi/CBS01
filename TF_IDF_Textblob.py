from __future__ import division, unicode_literals
import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


document1 = tb("""Today, the weather is 30 degrees in Celcius. It is really hot""")

document2 = tb("""I can't believe the traffic headed to the beach. It is really a circus out there.'""")

document3 = tb("""There are so many tolls on this road. I recommend taking the interstate.""")

bloblist = [document1, document2, document3]
for i, blob in enumerate(bloblist):
    print("Document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words:
        score_weight = score * 100 
        print("\t{}, {}".format(word, round(score_weight, 5)))