from collections import defaultdict
import random
word2num = {}
word2cands = {}

with open("data/test_input.txt") as f:
    for line in f:
        word, numclus, cands = line.split(" :: ")
        cands = cands.split()
        word2num[word] = int(numclus)
        word2cands[word] = cands

# random solution
out = open("test.random.solution", "w")

for word in word2cands:
    numclus = word2num[word]
    cands = word2cands[word]
    # in place
    random.shuffle(cands)
    clusters = []
    
    indices = sorted(random.sample(range(1,len(cands)), numclus-1))
    indices.insert(0,0)
    indices.append(len(cands))
    
    indpairs = list(zip(indices, indices[1:]))
    #print(indpairs)
    
    for p in indpairs:
        part = cands[p[0]:p[1]]
        clusters.append(part)
    
    #print(clusters)  
     
    for i, c in enumerate(clusters):    
        out.write(" :: ".join([word, str(i+1), " ".join(c)]) + "\n")

out.close()
print("Wrote random solution to: test.random.solution")

from gensim.models import KeyedVectors
import numpy as np
from sklearn.cluster import KMeans

# Downloaded from fasttext: https://fasttext.cc/docs/en/english-vectors.html
# Converted to word2vec binary format for faster loading (see convert.py)
#vec = KeyedVectors.load_word2vec_format("/home1/m/mayhew/data/wiki-news-300d-1M.vec.bin", binary=True)
#vec = KeyedVectors.load_word2vec_format("/home1/m/mayhew/data/GoogleNews-vectors-negative300.bin.filter")
vec = KeyedVectors.load_word2vec_format("data/coocvec-500mostfreq-window-3.vec.filter")
#vec = KeyedVectors.load_word2vec_format("data/GoogleNews-vectors-negative300.filter")
dim = vec.wv[vec.vocab.keys()[0]].shape[0]

out = open("test.coocvec.solution", "w")

for word in word2cands:

    print(word)
    
    cands = word2cands[word]
    X = np.zeros((len(cands), dim))
    for i, c in enumerate(cands):
        #print(vec.wv[c])
        if c in vec.wv:
            X[i] = vec.wv[c]
        else:
            print("{} is missing!".format(c))
            X[i] = np.random.rand(dim)

    kmeans = KMeans(n_clusters=word2num[word], random_state=0).fit(X)
    labelcands = zip(cands, kmeans.labels_)

    outcands = defaultdict(list)
    for p in labelcands:
        cand = p[0]
        ind = int(p[1]) + 1
        outcands[ind].append(cand)

    for item in sorted(outcands.items()):
        ind = item[0]
        out.write(" :: ".join([word, str(ind), " ".join(outcands[ind])]) + "\n")
    

out.close()
print("Wrote wordvec solution to: test.coocvec.solution")
            















