import gzip
from collections import defaultdict
import numpy as np

# Location of corpus
corpus = "reuters.rcv1.tokenized.gz"

# Word frequencies
freq = defaultdict(int)

# Calculate frequencies
i = 0
with gzip.open(corpus, "rt", encoding='utf8', errors="ignore") as f:
    for line in f:
        sline = line.strip().split()
        for token in sline:
            freq[token] += 1
        # Uncomment this for testing.
        # if i > 100000:
        #    break
        i += 1
total = i

# This maps the context words to integer (and vice versa)
D = 500
topD = sorted(freq.items(), key=lambda p: p[1], reverse=True)[:D]
topD_map = {}
topD_map_reverse = {}
for i, tup in enumerate(topD):
    word, wfreq = tup
    topD_map[word] = i
    topD_map_reverse[i] = word

# This maps word to integer (and vice versa)
vocab_map = {}
vocab_map_reverse = {}
for i, word in enumerate(freq):
    vocab_map[word] = i
    vocab_map_reverse[i] = word

# Now build term-context matrix
M = np.zeros((len(freq), D))
window = 3

k = 0
with gzip.open(corpus, "rt", encoding='utf-8', errors="ignore") as f:
    for line in f:
        sline = line.strip().split()

        for i in range(0, len(sline)):
            for j in range(i + 1, min(len(sline), i + window + 1)):
                if i == j: continue

                # add (i,j)
                token_id = vocab_map[sline[i]]
                context_token = sline[j]
                if context_token in topD_map:
                    context_token_id = topD_map[context_token]
                    M[token_id][context_token_id] += 1

                # add (j,i)
                token_id = vocab_map[sline[j]]
                context_token = sline[i]
                if context_token in topD_map:
                    context_token_id = topD_map[context_token]
                    M[token_id][context_token_id] += 1

        k += 1
        if k % 10000 == 0:
            print("Progress:", k / float(total))

        # Uncomment this for testing.
        # if k > 10000:
        #    break

# Write out to file.
with open("coocvec-{}mostfreq-window-{}.vec".format(D, window), "w") as out:
    out.write("{0} {1}\n".format(M.shape[0], M.shape[1]))
    for i, row in enumerate(M):
        out.write("{0} {1}\n".format(vocab_map_reverse[i], " ".join(map(lambda s: str(s), M[i]))))
