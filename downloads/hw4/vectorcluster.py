from gensim.models import KeyedVectors
import numpy as np
from sklearn.cluster import KMeans

# This maps from word  -> list of candidates
word2cands = {}

# This maps from word  -> number of clusters
word2num = {}

# Read the words file.
with open("data/dev_input.txt") as f:
    for line in f:
        word, numclus, cands = line.split(" :: ")
        cands = cands.split()
        word2num[word] = int(numclus)
        word2cands[word] = cands

# Load cooccurrence vectors (question 2)
vec = KeyedVectors.load_word2vec_format("data/coocvec-500mostfreq-window-3.vec.filter")
# Load dense vectors (uncomment for question 3)
# vec = KeyedVectors.load_word2vec_format("data/GoogleNews-vectors-negative300.filter")
        
for word in word2cands:
    cands = word2cands[word]
    numclusters = word2num[word]

    # TODO: get word vectors from vec
    # Cluster them with k-means
    # Write the clusters to file.

