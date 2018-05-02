'''
train_lm.py

Train a character-level ngram language model.

Usage:

python train_lm.py <CORPUSFILE> <OUTPUTFILE> (<ORDER>)
'''

import os, sys
import codecs

from collections import Counter, defaultdict

import util

def train_char_lm(fname, order=1, add_k=0.5):
    '''
    Train a character ngram language model.
    :param fname: string; filename containing corpus
    :param order: int; ngram length
    :param add_k: float; smoothing parameter
    
    :returns: dict; maps from n-grams of length order to a list of tuples. 
              Each tuple consists of a possible next character and its probability.
    '''

    data = codecs.open(fname, 'r', encoding='utf8', errors='replace').read()
    lm = defaultdict(Counter)
    vocab = set(list(data))
    pad = "~" * order
    data = pad + data
    
    # add OOV term
    vocab.add('<UNK>')
    
    for i in range(len(data)-order):
        history, char = data[i:i+order], data[i+order]
        lm[history][char]+=1
    
    # add k to each value
    for history, chars in lm.items(): 
        lm[history] = {k: v + add_k for k, v in chars.items()}
        # add unseen characters
        not_in_v = [v for v in vocab if v not in lm[history]]
        for v in not_in_v:
            lm[history][v] = add_k
    
    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c,cnt/(s + ((len(vocab) * add_k)))) for c,cnt in counter.items()] # adjusted denominator
    
    outlm = {hist:normalize(chars) for hist, chars in lm.items()}
    
    return outlm 


if __name__ == '__main__':
    
    corpusfile = sys.argv[1]
    model_output_file = sys.argv[2]
    if len(sys.argv) > 3:
        order = int(sys.argv[3])
    else:
        order = 1
    
    print('Training model')
    lm = train_char_lm(corpusfile, order=order)
    util.write_lm(lm, model_output_file)
