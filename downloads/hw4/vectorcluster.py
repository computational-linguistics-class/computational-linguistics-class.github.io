from pymagnitude import *


def load_file(file_path):
    word2cands = {}  # maps from word  -> list of candidates
    word2num = {}  # maps from word  -> number of clusters

    with open(file_path) as fin:
        for line in fin:
            word, num_clusters, candidates = line.split(" :: ")
            word2num[word] = int(num_clusters)
            word2cands[word] = candidates.split()

    return word2cands, word2num


def main():
    word2cands, word2num = load_file('data/dev_input.txt')

    # Load cooccurrence vectors (question 2)
    vectors = Magnitude("data/coocvec-500mostfreq-window-3.filter.magnitude")

    # Load dense vectors (uncomment for question 3)
    # vectors = Magnitude("data/GoogleNews-vectors-negative300.filter.magnitude")

    for word in word2cands:
        candidates = word2cands[word]
        num_clusters = word2num[word]

        # TODO:
        # 1. Get word vectors from vectors
        # 2. Cluster them with k-means
        # 3. Write the clusters to file.


if __name__ == '__main__':
    main()
